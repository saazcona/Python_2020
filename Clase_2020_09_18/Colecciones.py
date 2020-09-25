### Colecciones ### : Listas, Tuplas y Diccionarios

### Listas ###
# Se delimitan entre corchetes [ ]
notas = [90, 80, 70, 85]
#         0   1   2   3

print(notas)

# Para acceder a los valores se utilizan los indices

print(notas[3])

# Se pueden modificar los datos de los indices
notas[2] = 75
print(notas[2])

# Las listas son objetos y como objetos tienen una serie de atributos y metodos
# como el metodo append que agrega elementos a la lista
notas.append(100)
print(notas)

# remove en otra parte, los remueve
notas.remove(100)
print(notas)

nombres = []
nombres.append("Juan")
nombres.append("Mario")
nombres.append("Lucas")
nombres.append("MMG Moronta")

print(nombres)

# Para recorrer la lista completa se usa un ciclo for

# Con un ciclo while se haría...
# i = 0
# while(i < len(nombres)):
#     print(nombres[i])
#     i += 1

# Como el ciclo while utiliza muchas mas lineas de código, y depende de un indice para recorrer la lista
# el ciclo for entra en accion y simplifica esta metodologia

#El ciclo for nos permite iterar sobre una coleccion, es decir, se repetirá tantos elementos tenga
# lista

for nombre in nombres:
    print(nombre)

#Lo que hace el ciclo es que inicializa con la variable "nombre", en donde se iran almacenando
# los elementos de la coleccion

for nota in notas:
    print(nota)

# Es el uso mas comun y util del ciclo for

### Tuplas ###
# Las tuplas son inmutables, es decir, que no se pueden modificar
# Cuando definimos una tupla, esta se mantiene intacta
# No se le puede hacer append o remove
# Se utilizan los parentesis ( )

nombres_tuplas = ('Asta', 'Noelle', 'Secre')

for mitupla in nombres_tuplas:
    print(mitupla)

print(nombres_tuplas[1])

# Si se intenta agregar un elemento a una tupla...
# nombres_tuplas.append('No va a funcionar!!!')


### Diccionarios ###

# Nos permiten crear colecciones o más bien definir una estructura de datos formadas con un formato específico
# clave:valor
# Se definen con las llaves { }
# Los diccionarios son objetos

usuario = {
    'usuario': 'ffulgencio',
    'clave': '123456'
}

print(usuario['usuario'])

# Para obtener todas las claves del diccionario se usa .keys

print(usuario.keys())

# Para obtener todos los valores del diccionario se usa .values

print(usuario.values())