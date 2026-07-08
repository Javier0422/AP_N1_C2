import mysql.connector
from mysql.connector import Error

def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='biblioteca'
        )

        if conexion.is_connected():
            print("Conectado con base de datos MySQL")

            return conexion

    except Error as e:
        print(f"Error al conectar con MySQL: {e}")

    finally:
        if 'connection' in locals() and conexion.is_connected():
            conexion.close()
            print("Conexión con MySQL terminada.")

def insertar_datos(consulta):
    conexion = conectar_db()
    cursor = conexion.cursor()
    if cursor:
        cursor.execute(consulta)
        conexion.commit()
        print('Datos almacenados correctamente.')