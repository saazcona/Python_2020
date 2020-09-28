# Modulos

# Un módulo es un archivo con extensión .py que dentro de el están definidas varias funciones o clases
# que pueden utilizarse en otros módulos

# Se ha creado el archivo misfunciones.py

# from misfunciones import sumar, duplicar, ROJO

# print(sumar(2, 4))

# La funcion sumar no se encuentra en ese archivo, por eso se puede importar de otros archivos

# print(ROJO)

# Cuando escribimos una variable se escribe en mayúscula su valor se define una única vez y no se redifine
# es decir, no debe cambiarse

# Importando de otro modulo "Estudiantes"

#     archivo            clase creada
# from Estudiantes import Estudiante

# e1 = Estudiante("Maria", "Pantaloncillo")

# Importando del modulo "modelos"
# from modelos import *

# c1 = Curso()
# p1 = Profesor()

# Importar paquetes desde la carpeta mismodulos

from mismodulos import aritmetica

resultado = aritmetica.sumar(4,6)
print(resultado)