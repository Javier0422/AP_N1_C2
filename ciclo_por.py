# Ciclo For (por) para iterar Listas
# Recorro cada uno de los elementos de la lista

lista_bandas = ['P.O.D', 'Skillet', 'Demon Hunter']
nombre_personal = 'Javier Morales'

# Usamos el metodo RANGE para crear un rangom de numeros
# Si a RANGE le pasamos 1 argumento, creara una lista de numeros de la cantidad entregada
# La lista inicia en el indice 0
lista_numeros = range(5)

# Si a RANGE le pasamos 2 argumentos, le indicamos donde inicia y la cantidad de elementos
lista_numeros_2 = range(10,50)

# Si a RANGE le pasamos 3 argumentos, le indicamos donde inicia, el elemento final -1 y el avance entre nuemros
lista_numeros_3 = range(5,26,5)

for elemento in lista_bandas:
    print(elemento.upper())

for letra in nombre_personal:
    print(letra)

print(lista_numeros)
for numero in lista_numeros:
    print(elemento)

print()
print(lista_numeros_3)
for numero in lista_numeros_3:
    print(elemento)