# Práctica 1: Variables, Tipos de Datos, Expresiones y Condicionales
# Saul Azcona

# E1: Escriba en pantalla el tipo de dato que retorna la expresión 4 < 2

print(type(4 < 2))

# E2: Almacene en una variable el nombre de una persona y al final muestre en la consola el mensaje: “Bienvenido [ nombrePersona]”

nombre = "Saul Azcona"
print("Bienvenido " + nombre)

# E3: Evalúe si un número es par o impar y muestre en la consola el mensaje

numero = 11
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# E4: Almacene dos números y evalúe si el primero es mayor que el segundo. El resultado debe verse en la consola.

num1 = 5
num2 = 8

if num1 > num2:
    print(True)
else:
    print(False)

# E5: Convierta dólares a pesos

tasa = 58.03
dolar = 300

peso_dom = dolar * tasa
print(peso_dom)

# E6: Convierta grados celsius a Fahrenheit

grados_celsius = 25.5
grados_farenheit = 1.8 * grados_celsius + 32

print(grados_farenheit)

# E7: Almacene cuatro notas 90,95, 77,92 y las promedie. Al final debe decir su califica ción en letras A,B,C,D,E ó F.

nota_1 = 90
nota_2 = 95
nota_3 = 77
nota_4 = 92

promedio = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if promedio >= 90:
    print("A")
elif promedio >= 80:
    print("B")
elif promedio >= 70:
    print("C")
elif promedio >= 60:
    print("D")
else:
    print("F")

# E8: Que almacene monto, cantidad de cuotas, y porcentaje de interés anual de un préstamo y calcule la cuota mensual. (Amortizar mediante el sistema francés)

monto = 100000.00
n = 120
tasa = 0.10 / 12

cuota = monto * (pow(1 + tasa, n) * tasa) / (pow(1 + tasa, n) - 1)

print("El monto a pagar mensual es de: " + str(cuota))

