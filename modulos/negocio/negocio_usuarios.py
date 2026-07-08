from datos import listado_usuarios
from datos.data_usuarios import escribir_data_usuarios
from prettytable import PrettyTable
import bcrypt

def procesar_usuario(nombre, correo, telefono, rut, contrasena):
    password = contrasena.encode('utf-8')
    contrasena_encriptada = bcrypt.hashpw(password, bcrypt.gensalt())
    escribir_data_usuarios(nombre,correo,telefono,rut,contrasena_encriptada)

def crear_tabla_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = ['N°','Nombre','Email','Celular','RUT']

    for usuario in listado_usuarios:
        tabla_usuarios.add_row([usuario['id'],usuario['nombre'],usuario['correo'],usuario['telefono'],usuario['rut']])
    
    return tabla_usuarios

def buscar_usuario_nombre(nombre):
    for usuario in listado_usuarios:
        if usuario['nombre'].lower() == nombre.lower():
            return usuario

def buscar_usuario_correo(correo):
    for usuario in listado_usuarios:
        if usuario['correo'].lower() == correo.lower():
            return usuario
        
def bloquear_usuario(correo_usuario):
    for usuario in listado_usuarios:
        if usuario['correo'].lower() == correo_usuario.lower():
            usuario.update({'habilitado':False})
            escribir_data_usuarios(listado_usuarios)
            return True