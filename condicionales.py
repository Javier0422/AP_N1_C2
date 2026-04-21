str_edad = input('Ingrese su edad: ')
edad = int(str_edad)

#Condicional IF
if edad >= 18:
    #   Este set de acciones se ejecuta cuando la respuesta V
    print("UD. es mayor de edad.")
else:
    #   Este set de acciones se ejecuta cuando la respuesta F
    print("UD. es menor de edad.")
    
    #Solicite al ususario el igreso de datos personales (nombre, edad y titulo)
    #Si el uusario es mayor de edad, muestre por pantalla todos sus datos
    #Si el usuario es menor de edad, muestre un mensaje indicando que es menor de edad 

    nombre = int(input('Ingrese su nombre: '))
    edad = int(input('Ingrese su edad: '))
    titulo = int (input('Ingrese su titulo: '))
    
    if edad >= 18:
        print(nombre, edad, titulo)
    else:
        print("UD. es menor de edad.")

# Para evaluar varias condiciones usamos IF con ELIF

# Clase Alta ÉliteSobre $7.000.000
# Clase Alta Profesional $3.500.000 - $7.000.000
# Clase Media Alta $2.000.000 - $3.500.000
# Clase Media $1.200.000 - $2.000.000
# Clase Media Baja $700.000 - $1.200.000
# Clase Baja Menos de $600.000

str_sueldo_mensual = input('Ingrese su sueldo mensual: $')
sueldo_mensual = float(str_sueldo_mensual)

if str_sueldo_mensual.isdigit():
 sueldo_mensual = float(str_sueldo_mensual)
else:
 print('El valor ingresado No corresponde!')


if sueldo_mensual > 7000000:
    print('Ud. pertenece al grupo Alta Elite')
elif 3500000 < sueldo_mensual <= 7000000:
    print('Ud. pertenece al grupo Alta Profesional')
elif 2000000 < sueldo_mensual <= 3500000:
    print('Ud. pertenece al grupo Media Alta')
elif 1200000 < sueldo_mensual <= 2000000:
    print('Ud. pertenece al grupo Media Emergente')
elif 700000 < sueldo_mensual <= 1200000:
    print('Ud. pertenece al grupo Media Baja')
elif sueldo_mensual < 700000:
    print('Ud. pertenece al grupo Baja')
else:
    print('Sueldo ingresado NO corresponde...')   