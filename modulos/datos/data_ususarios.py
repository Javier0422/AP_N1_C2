import os
from datos import error_creacion,insertar_datos

def escribir_data_usuarios(nombre, correo,telefono,rut,contrasena):
    consulta = f"""INSERT INTO biblioteca.usuarios
    (nombre_usuario, correo_usuario, telefono_usuario, rut_usuario, contrasena, usuario_habilitado)
    VALUES({nombre}, {correo}, {telefono}, {rut}, {contrasena}, 1);"""

    insertar_datos(consulta)