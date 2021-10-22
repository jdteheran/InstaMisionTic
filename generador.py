import werkzeug.security as ws


#mensaje_encriptado = ws.generate_password_hash('pepito')

#print(mensaje_encriptado)

columna_password_bd = 'pbkdf2:sha256:260000$tiPlYKlI0R3uv6Fl$ccdfddde33f337d02c3ff33e780ada5d0d23b9d0e1dec475be2060e78c46b570'

auth = ws.check_password_hash(columna_password_bd, 'pepito')
print(auth)