nombre_personal = 'Javier Morales'
titulo_personal = 'Analista Programador'
ciudad = 'TEMUCO'

#El metodo DIR, nos indica los metodos disponibles para la variable
#print(dir(nombre_personal))

print(f'Su nombre personal CAPITALIZADO: {nombre_personal.capitalize()}')
print(f'Su nombre personal EN MAYÚSCULAS: {nombre_personal.upper()}')
print(f'Su nombre personal como TÍTULO: {nombre_personal.title()}')
print(f'Su ciudad EN MINÚSCULAS: {ciudad.lower()}')

print(titulo_personal.count('e'))