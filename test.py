
import sqlite3

conn = sqlite3.connect("jean.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT
    )
""")

cursor.execute("""
    INSERT INTO clientes (nombre, telefono)
    VALUES ('Mike Cardona', '664-510-61-45')
""")


conn.commit()
conn.close()