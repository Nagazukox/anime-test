import json
import sqlite3

# Leer el archivo JSON
with open("lista.json", "r") as archivo:
    lista = json.load(archivo)

# Crear la conexión con la base de datos
conexion = sqlite3.connect("anime.sqlite")
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS "animes" (
	    "id"	INTEGER,
	    "titulo"	TEXT,
	    "cap"	INTEGER,
	    "enlace"	TEXT,
	    "imagen"	TEXT,
	    PRIMARY KEY("id" AUTOINCREMENT)
    )
    '''
)

# Borrar todos los registros de la tabla 'animes'
cursor.execute('DELETE FROM animes')
cursor.execute('UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME="animes"')

# Añadir los datos a la base de datos
for item in lista:
    cursor.execute('''
    INSERT OR REPLACE INTO animes (titulo, cap, enlace, imagen)
    VALUES (?, ?, ?, ?)
    ''', (item['titulo'], item['capitulo'], item['enlace'], item['imagen']))

# Guardar los cambios
conexion.commit()

# Consultar todos los registros de la tabla 'users'
cursor.execute('SELECT * FROM animes')

# Mostrar todos los registros por pantalla
print('Datos de la base de datos:')
for row in cursor.fetchall():
    print(row)


conexion.close()

print("Datos guardados correctamente")