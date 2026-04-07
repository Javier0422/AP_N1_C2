# Las LISTAS son colecciones ordenadas y mutables,
# es decir, son modificables una vez creadas.
# Pueden almacenar elementos de diferentes tipos al mismo tiempo,
# ideales para almacenar una colección de datos que necesita ser modificada o accedida por índices.
# Almacena los datos en 2 espacios de memoria, el índice y el dato mismo.

print("\nTrabajando con LISTAS.\n======================")
lista = ["Armando Casas", True, 1.73]
print(lista)

print(type(lista))

print(lista[0])
print(lista[1])
print(lista[2])

print(type(lista[0]))
print(type(lista[1]))
print(type(lista[2]))

str_nombre = input('Ingrese su nombre: ')
lista[0] = str_nombre # Cambio válido, acceso al elemento por ÍNDICE
print(lista[0])
print(f"{lista}\n")

# Reemplace el segundo elemento de la lista por su edad
# La edad debe ser un numero entero

str_edad = input('Ingrese su edad: ')
lista[1] = int(str_edad) # Cambio válido, acceso al elemento por ÍNDICE
print(lista[1])
print(f"{lista}\n")

# Los DICCIONARIOS son colecciones no ordenadas de pares KEY : VALUE, usando 2 espacios de memoria.
# Permiten almacenar datos de manera que cada elemento pueda ser recuperado, actualizado o eliminado usando su clave.

print("Trabajando con DICCIONARIOS.\n============================")
diccionario = {
    'nombre_personal' : 'Armando Casas',
    'Está emocionado?' : True,
    'Altura' : 1.73
}
print(type(diccionario))
print(diccionario)
print(diccionario['nombre_personal'])
diccionario['nombre_personal'] = "Nuevo Valor" # Cambio válido, acceso al elemento por KEY
print(diccionario['nombre_personal'])
print(f"{diccionario}\n")