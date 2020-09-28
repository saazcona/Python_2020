# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PROYECTO FINAL: PROGRAMACIÓN PYTHON (PYT-01)
# Integrantes: Saul Azcona & Samuel Fernández
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ---------------------------------------------------------------------------------------
# OPCION 2
# Hacer un programa que funcione como mantenimiento de productos y categorías.
# El programa debe precargar 10 productos y cinco categorías al iniciar.
# Al iniciar el programa el usuario debe tener opciones que le permitan:
# 1 - Agregar un producto y su categoría
#   1.1 - Cuando elija agregar un producto o una categoría debe de pedir si desea agregar otro
# 2 - Buscar un producto y su categoría
# 3 - Actualizar un producto y su categoría
# 4 - Borrar un producto y su categoría.
# 5 - Listar todos los productos y categorías.
# 6 - Salir del programa

# Modele las características de categoría y producto que considere necesarias.
# El programa debe permitir buscar por id y por nombre de producto y categoría.
# Después de cada opción debe volver al menú.
# El programa solo terminara cuando el usuario elija salir.

# ---------------------------------------------------------------------------------------

# Paso 1: Importar el módulo de SQLite
import sqlite3

conn = sqlite3.connect("almacen.db")
cursor = conn.cursor()

# #################################################################################################
# DEFINICION DE FUNCIONES
# #################################################################################################

# Función para crear la tabla "Productos" en base de datos almance.db
def crear_tabla_productos():
    try:
        conn = sqlite3.connect("almacen.db")
        cursor = conn.cursor()

        qry_crear_tabla = """
        CREATE TABLE IF NOT EXISTS Productos (
            productID           INTEGER PRIMARY KEY AUTOINCREMENT,
            producto            TEXT UNIQUE NOT NULL,
            categoria           TEXT,
            precio_unitario     REAL
        );
        """
        
        cursor.execute(qry_crear_tabla)     # Ejecutar la consulta
        conn.commit()                       # Validar los cambios
        print("Tabla creada exitosamente")

    except sqlite3.OperationalError as error:
        print("La tabla Productos ya existe", error)
    finally:
        if(conn):
            # Cerrar la conexión
            conn.close()
    

# Función para insertar reigstros a la tabla productos
def insertar_registros(producto, categoria, precio):

    # Query de inserción de datos a la tabla
    try:
        conn = sqlite3.connect("almacen.db")
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO Productos (producto, categoria, precio_unitario) VALUES(?, ?, ?);
        """

        cursor.execute(insert_query, (producto, categoria, precio))
        conn.commit()   # Validar los cambios        
        print("Producto insertado exitosamente")
    except sqlite3.IntegrityError:
        print("Este producto ya está en el catálogo!")
    finally:
        if(conn):
            conn.close()


# Función para consultar un producto particular
def consultar(producto):
    # Variable para consultar en la base de datos
    consulta = """SELECT * FROM Productos WHERE producto = ?;"""

    # Cursor para ejecutar la consulta
    cursor.execute(consulta, (producto,))

    # Variable para mostrar los resultados de la consulta
    resultado = cursor.fetchall()

    for ress in resultado:
        print(ress)


def actualizar():
    update_qry = """
            UPDATE Productos
            SET producto = ?,
                categoria = ?,
            WHERE
                producto = ? AND categoria = ?
        """



# Función para consultar todos los registros
def seleccionar_datos():
    # Variable para consultar en la base de datos
    qry_seleccionar = """SELECT * FROM Productos;"""

    # Cursor para ejecutar la consulta
    cursor.execute(qry_seleccionar)

    # Variable para mostrar los resultados de la consulta
    resultado = cursor.fetchall()

    for ress in resultado:
        print(ress)


# insertar_registros('Teclado', 'Perifericos Entradas', 749.95)
# insertar_registros('Disco duro', 'Almacenamiento', 6000.00)
# insertar_registros('Cable USB', 'Cables', 150.00)
# insertar_registros('Cable HDMI', 'Cables', 250.00)
# insertar_registros('Monitor LED', 'Perifericos Salidas', 8500.00)
# insertar_registros('Módem', 'Comunicaciones', 1200.00)
# insertar_registros('Memoria USB', 'Almacenamiento', 500.00)
# insertar_registros('Audífonos', 'Perifericos Salidas', 800.00)
# insertar_registros('Cámara digital', 'Perifericos Entradas', 7600.00)

# #################################################################################################
# INICIO DE LA APLICACION
# #################################################################################################

estado = True # Variable condicional para detener el ciclo while

while estado:
    print()
    print("BASE DE DATOS ALMACEN")
    print("1 – Agregar nuevo producto y categoría")
    print("2 – Buscar un producto y su categoría")
    print("3 – Actualizar un producto y su categoría")
    print("4 – Borrar un producto y su categoría.")
    print("5 – Listar todos los productos y categorías")
    print("6 – Salir")

    opcion = ""
    while opcion not in ("1", "2", "3", "4", "5", "6"):
        opcion = input("---> ")

    if opcion == "1":
        # 1 - Agregar nuevo producto y categoría
        nom_product = input("Nuevo Producto: ")
        categoria = input("Categoria del producto: ")
        precioU = float(input("Precio Unitario: $"))

        insertar_registros(nom_product, categoria, precioU)


    elif opcion == "2":
        # 2 - Buscar un producto y su categoría
        nom_product = input("Producto a buscar: ")
        consultar(nom_product)


    elif opcion == "5":
        # 5 – Listar todos los productos y categorías
        seleccionar_datos()


    elif opcion == "6":
        # 6 - Salir de la aplicación
        estado = False

    else:
        print("Opción incorrecta, intente nuevamente")




