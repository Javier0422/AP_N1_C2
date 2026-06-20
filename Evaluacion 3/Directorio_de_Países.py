capitales = {
    "Chile": "Santiago",
    "Argentina": "Buenos Aires",
    "Peru": "Lima",
    "Colombia": "Bogota",
    "Mexico": "Ciudad de Mexico"
}

pais = input("Ingrese el nombre del país: ")

encontrado = False
for clave in capitales:
    if clave == pais:
        encontrado = True

if encontrado == True:
    print("La capital de", pais, "es", capitales[pais])
else:
    print("No se encontró información para el país", pais)