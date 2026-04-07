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
print(lista[2])
print(lista[1])

print(type(lista[0]))
print(type(lista[1]))
print(type(lista[2]))

#lista[1] = "Nuevo Valor" # Cambio válido, acceso al elemento por ÍNDICE
#print(lista[1])
#print(f"{lista}\n")