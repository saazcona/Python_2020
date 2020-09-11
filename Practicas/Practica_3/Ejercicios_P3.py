# ~~~~~~~~~~~~~~~~~~~~~~~~
# Práctica 3: Saul Azcona
# ~~~~~~~~~~~~~~~~~~~~~~~~

# 1- Hacer una función que potencie un número x a la y

# valor = 10
# potencia = 2

# Definición de la función con 2 parámetros
# def pontenciar(a, b):
#     x = a ** b
#     return print(x)

# pontenciar(valor, potencia)

# 2- Realizar una función que pida por pantalla un número del 1 al 10 y muestre
# por pantalla el número escrito en letras.

# def numeros_a_letras():
#     n = int(input("Dame un número del 1 al 10: "))

#     if n > 10:
#         print("Valiste vergas, te pedí un numero del 1 al 10")
#     elif n == 1:
#         print("Uno")
#     elif n == 2:
#         print("Dos")
#     elif n == 3:
#         print("Tres")
#     elif n == 4:
#         print("Cuatro")
#     elif n == 5:
#         print("Cinco")
#     elif n == 6:
#         print("Seis")
#     elif n == 7:
#         print("Siete")
#     elif n == 8:
#         print("Ocho")
#     elif n == 9:
#         print("Nueve")
#     elif n == 10:
#         print("Diez")

# numeros_a_letras()

# 3- Hacer una función que reciba un año como argumento y retorne
# verdadero si es bisiesto.

# def anio_bisiesto(a):

#     if a % 4 == 0:
#         if a % 100 == 0:
#             if a % 400 == 0:
#                 print(True)
#             else:
#                 print(False)
#         else:
#             print(True)
#     else:
#         print(False)

# anio_bisiesto(1900)
# anio_bisiesto(2012)
# anio_bisiesto(2020)
# anio_bisiesto(2021)
# anio_bisiesto(2022)
# anio_bisiesto(2023)
# anio_bisiesto(2024)

# 4- Crear una función que evalúe dos números y retorne verdadero si ambos números son iguales.

# def igualdad(x, y):
#     if x == y:
#         print(True)
#     else:
#         print(False)

# igualdad(1, 5)
# igualdad(2, 2)

# # Probando con operaciones aritméticas dentro de la función
# igualdad(10/2, 5)
# igualdad(pow(10, 2), 100)


# 5- Un número palindrómico se lee igual en ambos sentidos.
# El palíndromo más grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.
# Cree una función que encuentre el palíndromo más grande hecho del
# producto de dos números de 3 dígitos.

# Se define una primera funcion para comprobar si los numeros introducidos son palíndromos
def esPalindromo(num): 
    return str(num) == str(num)[::-1] 

# Funcion para encontrar el palíndromo más grande
def masGrande(num1, num2): 
    z = 0 
    for x in range(num2, num1, -1):
        for y in range(num2, num1, -1):
            if esPalindromo( x * y):
                if x * y > z:
                    z = x * y
    return z


print(masGrande(100,999))

# 6- Hacer una función que reciba una cedula como argumento y diga si la
# cedula es válida o no.

# def comprador_cedulas():
#     cedula = input("Introduzca la cedula a comprobar sin guiones: ")
#     # Se hace uso de la función len() para comprobar si la longitud de los caracteres es mayor que 11
#     if len(cedula) > 11:
#         print("Cédula incorrecta")
#     else:
#         print("Cédula válida")

# comprador_cedulas()

# 7- Hacer una función que reciba como argumento una lista de elementos
# numéricos y retorno otra lista con cada elemento de la primera lista
# duplicados.



# 8- Hacer una función que reciba un valor iniciar y uno final, y muestre en
# pantalla las tablas de multiplicar de los números múltiplos de 6 que hay
# entre el valor inicial y el valor final.

# def tabla_multiplicar_num6(v_inicial, v_final):

#     n = 6

#     if v_inicial > v_final:
#         print("Error: Valor Inicial debe ser menor al Valor Final")
#     else:
#         while v_inicial <= v_final:
#             res =  n * v_inicial
#             print(f"{n} X {v_inicial} = {res}")
#             v_inicial += 1

# # Del 5 al 8
# tabla_multiplicar_num6(1, 10)

# # Del 11 al 20
# tabla_multiplicar_num6(11, 20)

# # Si el inicial es mayor que el final
# tabla_multiplicar_num6(10, 1)