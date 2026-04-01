# Tipos de datos en Python

print(type(5))
print(type(3.2))
print(type("Hola"))
print(type(True))

# La variable numero_real almacenará un dato de número entero
numero_entero = 0
numero_decimal = 0.0
cadenta_texto = "Buen día queridos estudiantes!"
valor_booleano = False

print("mi primer mensaje en Python")

print()
print(numero_entero)
print(type(numero_entero))

print()
print(numero_decimal)
print(type(numero_decimal))

print()
print(cadenta_texto)
print(type(cadenta_texto))

print()
print(valor_booleano)
print(type(valor_booleano))

valor_booleano = 5 > 3
print()
print(valor_booleano)
print(type(valor_booleano))

# Concatenación de cadenas de texto
saludo = "Buen día querido "
nombre = "Javier Morales"
print()
print(saludo + nombre)

texto_una_linea_comillas_simples = 'texto de una línea'
texto_una_linea_comillas_dobles = "texto de una línea"

texto_multiples_lineas_comillas_simples = '''
linea 1 texto multiples lineas
linea 2 texto multiples lineas
linea 3 texto multiples lineas 
'''
texto_multiples_lineas_comillas_dobles = """
linea 1 texto multiples lineas
linea 2 texto multiples lineas
linea 3 texto multiples lineas 
"""

print(texto_multiples_lineas_comillas_dobles)