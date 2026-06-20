temperaturas = [21.5, 24.0, 19.8, 26.3, 22.1, 23.7, 20.4]

maxima = temperaturas[0]
minima = temperaturas[0]
suma = 0

for temp in temperaturas:
    if temp > maxima:
        maxima = temp
    if temp < minima:
        minima = temp
    suma = suma + temp

promedio = suma / len(temperaturas)

print("Temperatura máxima:", maxima, "°C")
print("Temperatura mínima:", minima, "°C")
print("Temperatura promedio:", promedio, "°C")