import sqlite3

conn = sqlite3.connect('DB_dataseba.db')
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,45
        name TEXT NOT NULL,
        email CHAR(50) NOT NULL,
        password CHAR(250) NOT NULL
    )
''')

conn.commit()
conn.close()
