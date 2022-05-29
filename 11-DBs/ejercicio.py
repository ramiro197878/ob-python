# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará
# de tres columnas: la columna id de tipo entero, la columna nombre que será de
# tipo texto y la columna apellido que también será de tipo texto.

# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que
# insertar 8 alumnos a la tabla.

# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar
# los datos por consola.

import sqlite3

def crear_db():
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE alumnos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL);
            ''')

    cursor.close()
    conn.close()

def insertar_alumno():
    alumnos = [
            (1, 'Alejandro', 'Rodriguez'),
            (2, 'Ana', 'Garcia'),
            (3, 'David', 'Fernandez'),
            (4, 'Carmen', 'Alonso'),
            (5, 'Isabel', 'Romero'),
            (6, 'Daniel', 'Diaz'),
            (7, 'Marta', 'Perez'),
            (8, 'Pedro', 'Sanchez'),
            (9, 'Laura', 'Lopez'),
            (10, 'Miguel', 'Moreno')
            ]
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    query = ('INSERT INTO alumnos(id, nombre, apellido) VALUES(?, ?, ?)')

    cursor.executemany(query, alumnos)

    conn.commit()

    cursor.close()
    conn.close()




def main(nombre):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM alumnos WHERE nombre ="{nombre}"')

    rows = cursor.fetchall()

    for row in rows:
        print(row)



    cursor.close()
    conn.close()





if __name__ == "__main__":
    #crear_db()
    #insertar_alumno()
    main("Alejandro")
