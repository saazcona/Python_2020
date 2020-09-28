# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# PRACTICA V PYTHON - Saul Azcona
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Usando lo aprendido hasta ahora:
# Hacer un programa con acceso a base de datos que sirva como una agenda telefónica.
# Debe tener un menu que permita:

# 1 – Agregar nuevo contacto
# 2 – Listar todos los contactos
# 3 – Buscar contactos por nombre o numero de teléfono
# 4 – Actualizar un contacto
# 5 – Eliminar un contacto
# 6 – Salir

# Al agregar un nuevo contacto, debe validar que el contacto no exista previamente.
# Si existe debe dar un mensaje notificando al usuario.
# Al terminar de agregar un contacto debe preguntar si desea agregar otro.

agenda = {}

estado = True

while estado:
    print()
    print("AGENDA TELEFÓNICA")
    print("1 – Agregar nuevo contacto")
    print("2 – Listar todos los contactos")
    print("3 – Buscar contactos por nombre o numero de teléfono")
    print("4 – Actualizar un contacto")
    print("5 – Eliminar un contacto")
    print("6 – Salir")

    opcion = ""
    while opcion not in ("1", "2", "3", "4", "5", "6"):
        opcion = input("---> ")

    if opcion == "1":
        # 1 - Agregar un contacto nuevo
        nombre_contacto = input("Nuevo contacto: ")
        if nombre_contacto in agenda:
            print("Contacto está en la agenda!")
        else:
            telf_contacto = int(input("Nuevo teléfono: "))
            agenda[nombre_contacto] = telf_contacto
            print("Contacto añadido exitosamente")

    elif opcion == "2":
        # 2 - Mostrar todos los contactos
        print("Listando todos los contactos...\n")
        print(agenda.items())

    elif opcion == "3":
        # 3 - Buscar contactos por nombre o numero telefónico
        buscar_contacto = input("Contacto a buscar: ")
        if buscar_contacto not in agenda:
            print("El contacto no existe en la agenda")
        else:
            telefono = agenda[buscar_contacto]
            print(buscar_contacto, " : ", telefono)

    elif opcion == "4":
        # 4 - Actualizar un contacto
        nombre_contacto = input("Contacto a actualizar: ")
        if nombre_contacto not in agenda:
            print("El contacto no existe en la agenda")
        else:
            telf_contacto = int(input("Nuevo teléfono: "))
            agenda[nombre_contacto] = telf_contacto
            print("Teléfono de ", nombre_contacto, " ha sido actualizado")

    elif opcion == "5":
        # 5 – Eliminar un contacto
        nombre_contacto = input("Contacto a borrar: ")
        if nombre_contacto not in agenda:
            print("El contacto no existe en la agenda")
        else:
            agenda.pop(nombre_contacto)
            print("El contacto ha sido eliminado")

    elif opcion == "6":
        # 6 - Salir de la aplicación
        estado = False