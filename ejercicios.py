#1- Escriba una funcion que calcule el total de una factura tras aplicarle el IVA
#    La funcion debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
#    si la funcion no recibe el porcentaje de IVA, deberá apicar por defecto un 19%

#2- Ecriba una funcion que calcule el área de un círculo y otra que calcule
#   el volumen de un cilindro usando la primera FUNCION DE Área

# 3.- Escriba una función que permita escribir la tabla de multiplicar de un número ingresado por el usuario.

#1
#def calcular_total_con_iva(cantidad_sin_iva, porcentaje_iva=19):
#    iva = cantidad_sin_iva * (porcentaje_iva / 100)
#    total_con_iva = cantidad_sin_iva + iva
#    return total_con_iva
#cantidad = float(input('Ingrese la cantidad sin IVA: '))
#iva_porcentaje = input('Ingrese el porcentaje de IVA (o deje en blanco para usar el 19% por defecto): ')
#if iva_porcentaje == '':
#    iva_porcentaje = 19
#else:    iva_porcentaje = float(iva_porcentaje)

#total = calcular_total_con_iva(cantidad, iva_porcentaje)
#print(f"El total con IVA es: {total}")

#2
#area_circulo = float(input('Ingrese el radio del círculo para calcular su área: '))
#radio_elev = area_circulo * area_circulo
#area = 3.1416 * radio_elev
#print(f"El área del círculo es: {area}")

#altura_cilindro = float(input('Ingrese la altura del cilindro para calcular su volumen: '))
#radio_cilindro = float(input('Ingrese el radio del cilindro para calcular su volumen: '))
#area_base = 3.1416 * (radio_cilindro * radio_cilindro)
#volumen_cilindro = area_base * altura_cilindro
#print(f"El volumen del cilindro es: {volumen_cilindro}")

#3
#def mostrar_tabla_multiplicar(numero):
#    print(f"Tabla de multiplicar del {numero}:")
#    for i in range(1, 11):
#        resultado = numero * i
#        print(f"{numero} x {i} = {resultado}")

while True:
    print('\nIngrese el ejercicio que desea ejecutar:')
    print('[1] Calcular total con IVA')
    print('[2] Calcular área de un círculo y volumen de un cilindro')
    print('[3] Mostrar tabla de multiplicar')
    print('[0] Salir')
    opcion = input('Seleccione una opción [0-3]: ')

    if opcion == "1":
        cantidad = float(input('Ingrese la cantidad sin IVA: '))
        iva_porcentaje = input('Ingrese el porcentaje de IVA (o deje en blanco para usar el 19% por defecto): ')
        if iva_porcentaje == '':
            iva_porcentaje = 19
        else:
            iva_porcentaje = float(iva_porcentaje)
        total = calcular_total_con_iva(cantidad, iva_porcentaje)
        print(f"El total con IVA es: {total}")

    elif opcion == "2":
        radio = float(input('Ingrese el radio del círculo para calcular su área: '))
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area}")
        altura_cilindro = float(input('Ingrese la altura del cilindro para calcular su volumen: '))
        volumen = calcular_volumen_cilindro(radio, altura_cilindro)
        print(f"El volumen del cilindro es: {volumen}")

    elif opcion == "3":
        numero = int(input('Ingrese un número para mostrar su tabla de multiplicar: '))
        mostrar_tabla_multiplicar(numero)

    elif opcion == "0":
        break
    else:
        print("Opción no válida")
