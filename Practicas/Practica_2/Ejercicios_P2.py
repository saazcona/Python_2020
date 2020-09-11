# ~~~~~~~~~~~~~~~~~~~~~~~~
# Práctica 2: Saul Azcona
# ~~~~~~~~~~~~~~~~~~~~~~~~

# 1 – Realizar un programa que solicite al usuario un número indeterminado de
# números (mientras se tecleen números que no sean cero). Al salir el programa
# debe dar en pantalla el total de números dados y la suma de ellos.

numero_solicitado = input("Dame un numero: ")   # Variable para solicitar los datos
acum = 0    # Variable acumuladora

# Mientras el número solicitado NO sea cero
while int(numero_solicitado) != 0:
    numero = int(numero_solicitado)
    acum += numero
    numero_solicitado = input("Dame un numero: ")

# Se imprime el resultado final de la variable acumulada
print("Suma Total: " + str(acum))

# 2- Realizar un programa que presente un menú con las siguientes opciones
#   1- Convertir grados a Celsius a Fahrenheit
#   2- Convertir dólar a pesos
#   3- Convertir metros a pies
#   4- Salir
#
# Cada vez que finalice una de estas acciones debe regresar al menú. El programa
# solo finalizará cuando el usuario elija la opción salir.

x = 0   # Variable inicial para condicionar el while

# Mientras la variable no sea la opción 4
while x != 4:

    sel_opcion = float(input("Convertir \n" + "1-Grados Celsius a Fahrenheit\n" + "2-Dólar a Pesos\n" + "3-Metros a Pies\n" + "4-Salir\n"))

    # Opcion 1: Convertir de ºC a ºF
    if sel_opcion == 1:
        grados_celsius = input("Introducir grados celsius: ")
        grados_farenheit = 1.8 * float(grados_celsius) + 32.0
        print(str(grados_farenheit) + " ºF\n")
    # Opción 2: Convertir Dólares a pesos dominicanos
    elif sel_opcion == 2:
        dolar = input("Dólares a cambiar: ")
        tasa = 58.03    # tasa escogida aleatoriamente
        peso_dom = float(dolar) * tasa
        print(str(peso_dom) + " DOP\n")
    # Opción 3: Convertir Metros a Pies
    elif sel_opcion == 3:
        m = input("Cantidad de metros a convertir: ")
        ft = 3.28084
        m_to_ft = float(m) * ft
        print(str(m_to_ft) + " ft\n")
    # Si no existe la opcion...
    else:
        print("\nOpcion no existe\n")
    
    x = sel_opcion

print("\nGracias por utilizar nuestro conversor\n")


# 3- Hacer un programa que genere las tablas de multiplicar de los números múltiplos
# de 5 que hay entre 1 y 1000

n = 5
c = 1
while c <= 1000:
    res =  n * c
    print(f"{n} X {c} = {res}")
    c += 1

# 4- Realizar un programa que reciba por teclado el sueldo de un empleado y le
# aplique los cálculos de ISR (ver tabla DGII), ARS, y AFP (investigar porcentajes)

# Calculadora de ISR

top1 = 416220.00
top2 = 624329.00
top3 = 867123.00

salario = float(input("Ingrese el sueldo mensual: "))
salario_anual = salario * 12

isr = 0
ars = 0
afp = 0

if salario_anual <= top1:
    print("Excenta")

elif salario_anual <= top2:
    excedente = salario_anual - top1
    isr = excedente * 0.15

elif salario_anual <= top3:
    excedente = salario_anual - top2
    isr = 31216.00 + excedente * 0.20

else:
    excedente = salario_anual - top3
    isr = 79776.00 + excedente * 0.25

isr = isr / 12
afp = salario * 0.0287
ars = salario * 0.0304

print("ISR: " + str(isr))
print("AFP: " + str(afp))
print("ARS: " + str(ars))


# 5-Cree una aplicación de cajero automático para el banco ABC. El cajero tendrá un
# límite de billetes descrito a continuación: 9 de 1000, 19 de 500, 99 de 100

# El cajero debe solicitar Banco y monto a retirar. Si el banco es ABC el limite de
# retiro son 10,000 y 2000 pesos por transacción en caso contrario.

# El cajero debe informar si el monto solicitado no puede ser dispensado o si
# excede el límite de transacción. Y debe hacer la distribución de los billetes de
# acuerdo al monto. Por ejemplo, si el usuario solicita 3,900 y hay disponibilidad en
# todos los billetes, el cajero debe dispensar 3 billetes de mil, 1 de quinientos y 4 de cien.

bill_de_1000 = 9
bill_de_500 = 19
bill_de_100 = 99

# Variables dispensadores de billetes
de_1000 = 0
de_500 = 0
de_100 = 0

max_ABC = 10000     # Límite máximo para dispensar efectivo con Banco ABC

# Variable inicial para solicitar opción deseada
opciones = int(input("Bienvenido\n" + "1 - Banco ABC\n" + "2 - Otro banco\n" + "3 - Salir\n"))

# Si el banco es ABC (opcion 1)
if opciones == 1:
    #   Solicitar el monto a dispensar
    print("Este cajero sólo dispensa billetes de RD$1,000, de RD$500 y de RD$100")
    billetico = int(input("\nMonto a retirar: "))

    # Si el monto es mayor a 1000 o si el monto es impar no dispensa el efectivo
    if (billetico >= max_ABC) or (billetico % 2 != 0):
        print("El monto solicitado no puede ser dispensado")
    else:
    #    Ciclo while para dispensar billetes de 1000
        while billetico >= 1000:
            de_1000 += 1
            billetico -= 1000
        print("Billetes de $1000: " + str(de_1000))
    #    Ciclo while para dispensar billetes de 500
        while billetico >= 500:
            de_500 += 1
            billetico -= 500
        print("Billetes de $500: " + str(de_500))
    #    Ciclo while para dispensar billetes de 100
        while billetico >= 100:
            de_100 += 1
            billetico -= 100
        print("Billetes de $100: " + str(de_100))

# Si no es el Banco ABC entonces:
elif opciones == 2:
    print("Este cajero sólo dispensa billetes de RD$1,000, de RD$500 y de RD$100")
    #   Solicitar el monto a dispensar
    billetico = int(input("\nMonto a dispensar: "))
    # if condicional para verificar si el monto es superior a 2000
    if billetico > 2000:
        print("Solo $2,000 por transacción")
    else:
        while billetico >= 1000:
            de_1000 += 1
            billetico -= 1000
        print("Billetes de 1000: " + str(de_1000))

        while billetico >= 500:
            de_500 += 1
            billetico -= 500
        print("Billetes de 500: " + str(de_500))

        while billetico >= 100:
            de_100 += 1
            billetico -= 500
        print("Billetes de 100: " + str(de_100))

# Condicion en caso de que se introduzca un valor equivocado
elif opciones == 3:
    print("Gracias por utilizar nuestro cajero")

else:
    print("Opción incorrecta, seleccione otra opción nuevamente\n")