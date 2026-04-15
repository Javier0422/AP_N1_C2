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

