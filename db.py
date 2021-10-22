import sqlite3
from sqlite3 import Error

def obtener_conexion():
    try:
        conexion = sqlite3.connect('db/basedatos.db')
        return conexion
    except Error:
        print(Error)


def obtener_registros(tabla, condicion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    if condicion == None:
        strsql = 'SELECT * FROM {}'.format(tabla)
    else:
        strsql = 'SELECT * FROM {} WHERE {}'.format(tabla, condicion)

    cursor.execute(strsql)

    datos = cursor.fetchall()
    conexion.close()

    return datos

def insertar_usuario(nombre, usuario, correo, contrasena):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    strsql = "INSERT INTO usuario (nombre, usuario, correo, contrasena) VALUES ('{}', '{}', '{}', '{}')".format(nombre, usuario, correo, contrasena)

    cursor.execute(strsql)
    conexion.commit()
    conexion.close()

def insertar_image_usuario(id_usuario, imagen):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    strsql = "INSERT INTO imagenUsuario (id_usuario, imagen) VALUES ({}, '{}')".format(id_usuario, imagen)

    cursor.execute(strsql)
    conexion.commit()
    conexion.close()

def actualizar_avatar_usuario(usuario, avatar):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    strsql = 'UPDATE usuario SET avatar = {} WHERE usuario = {}'.format(usuario, avatar)

    cursor.execute(strsql)
    conexion.commit()
    conexion.close()