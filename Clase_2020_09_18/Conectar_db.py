# Conectar python con sqlite3

# Pasos para trabjar con una db
# 1 - Importar el módulo con el que trabajaremos
import sqlite3

# 2 - Crear una conexion a la base de datos
conn = sqlite3.connect("mydb.db")

# 3 - Crear una variable intermedia que nos permita enviar consultas
cursor = conn.cursor()

query1 = """
CREATE TABLE Estudiantes (nombre text, apellido text);
"""
query2 = """
INSERT INTO Estudiantes VALUES('Nico', 'Robin');
"""
query3 = """
SELECT * FROM Estudiantes;
"""

# cursor.execute(query1)
# cursor.execute(query2)
cursor.execute(query3)

resultado = cursor.fetchall()
print(resultado)

for ress in resultado:
    print(ress[0])

# 4 - Validar los cambios
conn.commit()

# 5 - Cerrar la conexión
conn.close()