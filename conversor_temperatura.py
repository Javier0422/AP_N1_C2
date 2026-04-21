# Teniendo 3 escalas de temperatura (Celsius, Fahrenheit y Kelvin)
# Cree un conversor de temperatura que le pida al usuario la temperatura y escla inicial
# Y la escala a la que desea convertir, luego muestre el resultado de la conversión

# °C a F = 1,8 * °C + 32
#  F a °C = 5/9(°F - 32°

# °C a K = °C + 273°)
# K a °C = K - 273°

# K a F = (1,8° C +32°) + 273°
# F a K = (5/9(°F - 32°) + 273°

str_temperatura = input('Ingrese la temperatura a convertir: ')
Temperatura = float (str_temperatura)

if str_temperatura.isdigit():
    temperatura = float(str_temperatura)
else:
    print('El valor ingresado No corresponde!')

print('Ingrese la escala inicial de la temperatura: ')
print('1. Celsius')
print('2. Fahrenheit')
print('3. Kelvin')
str_escala_inicial = input('Ingrese el número correspondiente a la escala inicial: ')
if str_escala_inicial.isdigit():
    escala_inicial = int(str_escala_inicial)
else:
    print('El valor ingresado No corresponde!')

print('Ingrese la escala a la que desea convertir: ')
print('1. Celsius') 
print('2. Fahrenheit')
print('3. Kelvin')

str_escala_final = input('Ingrese el número correspondiente a la escala final: ')
if str_escala_final.isdigit():
    escala_final = int(str_escala_final)
else:
    print('El valor ingresado No corresponde!')

if escala_inicial == 1 and escala_final == 2:
    resultado = 1.8 * temperatura + 32
    print(f'{temperatura}°C es igual a {resultado}°F')
elif escala_inicial == 1 and escala_final == 3:
    resultado = temperatura + 273
    print(f'{temperatura}°C es igual a {resultado}K')
elif escala_inicial == 2 and escala_final == 1:
    resultado = 5/9 * (temperatura - 32)
    print(f'{temperatura}°F es igual a {resultado}°C')
elif escala_inicial == 2 and escala_final == 3:
    resultado = (5/9 * (temperatura - 32)) + 273
    print(f'{temperatura}°F es igual a {resultado}K')
elif escala_inicial == 3 and escala_final == 1:
    resultado = temperatura - 273
    print(f'{temperatura}K es igual a {resultado}°C')
elif escala_inicial == 3 and escala_final == 2:
    resultado = (1.8 * (temperatura - 273)) + 32
    print(f'{temperatura}K es igual a {resultado}°F')
else:    print('La conversión no es válida!')