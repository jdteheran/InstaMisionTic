from flask import Flask, render_template, request, redirect, jsonify, send_file, session
import db, io, werkzeug.security as ws

app = Flask(__name__)
app.secret_key = 'mi_llave_secreta'

@app.before_request
def antes_peticion():
    if 'usuario' not in session and request.endpoint in ['perfil']:
       return redirect('/')

    elif 'usuario' in session and request.endpoint in ['inicio', 'registro']:
        return redirect('/perfil/{}'.format(session['usuario']))


@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'GET':
        return render_template('inicio_sesion.html')
    else:
        usuario = request.form['usuario']
        registro_usaurio = db.obtener_registros('usuario', "usuario='{}'".format(usuario))
        contrasena_bd = registro_usaurio[0][4]
        if registro_usaurio is not None:
            contrasena = request.form['contrasena']
            contrasenas_iguales = ws.check_password_hash(contrasena_bd, contrasena)
            if contrasenas_iguales:
                session['usuario'] = usuario
                return redirect('/perfil/{}'.format(usuario))
        
        return render_template('inicio_sesion.html')
       

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'GET':
        return render_template('registro.html')
    else:
        #VALIDAR LOS VALORES DE LOS FORMULARIOS
        nombre = request.form['nombre']
        usuario = request.form['usuario']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        confirmar_contrasena = request.form['confirmar_contrasena']
        db.insertar_usuario(nombre, usuario, correo, ws.generate_password_hash(contrasena))
        session['usuario'] = usuario
        return redirect('/perfil/{}'.format(usuario))


@app.route('/perfil')
@app.route('/perfil/<usuario>')
def perfil(usuario=None):
    if usuario:
        registro_usaurio = db.obtener_registros('usuario', "usuario='{}'".format(usuario))

        if registro_usaurio:
            id_usuario = registro_usaurio[0][0]

            registro_imagenes = db.obtener_registros('imagenUsuario', "id_usuario={}".format(id_usuario))

            agregar = False
            if usuario == session['usuario']:
                agregar = True

            return render_template('perfil.html', usuario=registro_usaurio, registro_imagenes = reversed(registro_imagenes), agregar = agregar)
        else:
            usuario = session['usuario']
            return redirect('/perfil/{}'.format(usuario))     
    else:
        return render_template('perfil.html')


@app.route('/insertarImg/<usuario>', methods=['POST'])
def insertar_imagen(usuario):
    registro_usaurio = db.obtener_registros('usuario', "usuario='{}'".format(usuario))

    id_usuario = registro_usaurio[0][0]
    imagen = request.data.decode().replace('\n', ' ').replace('\r', '')

    db.insertar_image_usuario(id_usuario, imagen)

    return jsonify("imagen guardada exitosamente")

@app.route('/imagen/<int:id>')
def render_imagen(id):
    print('id={}'.format(id))
    imagen_registro = db.obtener_registros('imagenUsuario', 'id={}'.format(id))

    image_bytes = imagen_registro[0][2]

    bytes_io = io.BytesIO(image_bytes.encode())

    return send_file(bytes_io, mimetype='image/svg+xml')  

@app.route('/cerrar_sesion')
def cerrar_sesion():
    if 'usuario' in session:
        session.pop('usuario')
        return redirect('/')