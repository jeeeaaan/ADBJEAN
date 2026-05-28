"""
NIVEL 1 — Ejercicios completos
Esquema: Estudiantes / Cursos

Antes de empezar, crea la DB ejecutando el setup al final de este archivo.
Cada función tiene un ejercicio. Completa las líneas con "pass".

Para ver las soluciones, ejecuta:
    python 03_ejercicios.py --soluciones
"""

import sqlite3
import sys

DB_PATH = "escuela.db"


def conectar():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# =========================================================
# EJERCICIOS - SELECT
# =========================================================

def select_01():
    """Mostrar todos los datos de todos los estudiantes."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM estudiantes
    """)  # <-- completa aquí
    for r in cursor.fetchall():
        print(dict(r))
    conn.close()


def select_02():
    """Mostrar nombre, apellido y email de estudiantes nacidos después del 2001."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nombre, apellido, email FROM estudiantes 
        WHERE fecha_nacimiento > '2001-12-31'
    """)  # <-- completa aquí
    for r in cursor.fetchall():
        print(dict(r))
    conn.close()


def select_03():
    """Mostrar nombre y créditos de los cursos ordenados por créditos descendente."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nombre, creditos FROM cursos 
        ORDER BY creditos DESC
    """)  # <-- completa aquí
    for r in cursor.fetchall():
        print(dict(r))
    conn.close()


def select_04():
    """Mostrar nombre del estudiante, nombre del curso y nota (JOIN)."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.nombre as nombreEstudiante, c.nombre as nombreCurso, i.nota FROM estudiantes e
        INNER JOIN inscripciones i 
            ON e.id = i.estudiante_id
        INNER JOIN cursos c 
            ON c.id = i.curso_id
    """)  # <-- completa aquí
    for r in cursor.fetchall():
        print(dict(r))
    conn.close()


def select_05():
    """Mostrar cuántos estudiantes hay (columna: total)."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(nombre) as total FROM estudiantes
    """)  # <-- completa aquí
    print(dict(cursor.fetchone()))
    conn.close()


# =========================================================
# EJERCICIOS - INSERT
# =========================================================

def insert_01():
    """Insertar estudiante: María Torres, maria.torres@email.com, 2004-08-12."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO estudiantes (nombre, apellido, email, fecha_nacimiento)
        VALUES ('María', 'Torres', 'maria.torres@email.com', '2004-08-12')
    """) # <-- completa aquí
    conn.commit()
    print("[OK] Estudiante insertado.")
    conn.close()


def insert_02():
    """Insertar curso: Historia del Arte, créditos 3."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cursos (nombre, creditos)
        VALUES ('Historia del Arte',  3)
    """)  # <-- completa aquí
    conn.commit()
    print("[OK] Curso insertado.")
    conn.close()


def insert_03():
    """Inscribir a Ana López (id=1) en Bases de Datos (id=3)."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO inscripciones (estudiante_id, curso_id)
        VALUES (1, 3)
    """)  # <-- completa aquí
    conn.commit()
    print("[OK] Inscripcion insertada.")
    conn.close()


def insert_04():
    """Insertar dos estudiantes a la vez: Valentina Ruiz y Mateo Torres."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO estudiantes (nombre, apellido, email, fecha_nacimiento)
        VALUES ('Valentina', 'Ruiz', 'valentina.ruiz@email.com', '2003-01-30'),
            ('Mateo', 'Torres', 'mateo.torres@email.com', '2002-03-12')
    """)  # <-- completa aquí
    conn.commit()
    print("[OK] Estudiantes insertados.")
    conn.close()


# =========================================================
# EJERCICIOS - UPDATE
# =========================================================

def update_01():
    """Actualizar email de Carlos Mendoza (id=2) a carlos.m@email.com."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE estudiantes SET email = 'carlos.m@email.com'
        WHERE id = 2; 
    """)  # <-- completa aquí
    conn.commit()
    print("[OK] Email actualizado.")
    conn.close()


def update_02():
    """Cambiar créditos de Inglés Técnico (id=4) a 3."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE cursos SET creditos = 3
        WHERE id = 4; 
    """)  # <-- completa aquí
    conn.commit()
    print("[OK] Creditos actualizados.")
    conn.close()


def update_03():
    """Poner nota 14.5 a Sofía Ramírez (id=5) en Programación Python (curso_id=2)."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE inscripciones SET nota = 14.5
        WHERE estudiante_id = 5 AND curso_id = 2; 
    """)  # <-- completa aquí
    conn.commit()
    print("[OK] Nota actualizada.")
    conn.close()


# =========================================================
# EJERCICIOS - DELETE
# =========================================================

def delete_01():
    """Eliminar la inscripción con id=5."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM inscripciones
        WHERE id = 5;
    """)  # <-- completa aquí
    conn.commit()
    print("[OK] Inscripcion eliminada.")
    conn.close()


def delete_02():
    """Eliminar inscripciones con nota NULL."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM inscripciones
        WHERE nota is NULL;
    """)  # <-- completa aquí
    conn.commit()
    print(f"[OK] {cursor.rowcount} inscripcion(es) eliminada(s).")
    conn.close()


def delete_03():
    """Eliminar cursos sin estudiantes inscritos (usar NOT IN)."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM cursos
        WHERE id NOT IN (SELECT curso_id FROM inscripciones);
    """)  # <-- completa aquí
    conn.commit()
    print(f"[OK] {cursor.rowcount} curso(s) eliminado(s).")
    conn.close()






# =========================================================
# SETUP: crear DB con datos
# =========================================================

def crear_db():
    import os
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    conn.executescript("""
        CREATE TABLE estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            fecha_nacimiento DATE NOT NULL,
            fecha_inscripcion DATE DEFAULT CURRENT_DATE
        );
        CREATE TABLE cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            creditos INTEGER NOT NULL CHECK(creditos > 0)
        );
        CREATE TABLE inscripciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            estudiante_id INTEGER NOT NULL,
            curso_id INTEGER NOT NULL,
            fecha_inscripcion DATE DEFAULT CURRENT_DATE,
            nota REAL CHECK(nota >= 0 AND nota <= 20),
            FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
            FOREIGN KEY (curso_id) REFERENCES cursos(id)
        );
        INSERT INTO estudiantes VALUES
            (1, 'Ana', 'López', 'ana.lopez@email.com', '2002-03-15', '2024-03-01'),
            (2, 'Carlos', 'Mendoza', 'carlos.mendoza@email.com', '2001-07-22', '2024-03-01'),
            (3, 'Lucía', 'Fernández', 'lucia.fernandez@email.com', '2003-01-10', '2024-03-01'),
            (4, 'Pedro', 'García', 'pedro.garcia@email.com', '2000-11-05', '2024-03-01'),
            (5, 'Sofía', 'Ramírez', 'sofia.ramirez@email.com', '2002-09-18', '2024-03-01');
        INSERT INTO cursos VALUES
            (1, 'Matemáticas I', 'Álgebra y cálculo', 5),
            (2, 'Programación en Python', 'Introducción con Python', 4),
            (3, 'Bases de Datos', 'Bases relacionales', 4),
            (4, 'Inglés Técnico', 'Inglés aplicado a tecnología', 2);
        INSERT INTO inscripciones (id, estudiante_id, curso_id, fecha_inscripcion, nota) VALUES
            (1, 1, 1, '2024-03-05', 18.5),
            (2, 1, 2, '2024-03-05', 16.0),
            (3, 2, 1, '2024-03-06', 14.0),
            (4, 2, 3, '2024-03-06', 17.5),
            (5, 3, 2, '2024-03-07', 19.0),
            (6, 3, 3, '2024-03-07', 15.5),
            (7, 4, 1, '2024-03-08', 12.0),
            (8, 4, 4, '2024-03-08', 18.0),
            (9, 5, 2, '2024-03-09', NULL),
            (10, 5, 3, '2024-03-09', NULL);
    """)
    conn.commit()
    conn.close()
    print(f"[OK] Base de datos '{DB_PATH}' creada.\n")


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":
    if "--soluciones" in sys.argv:
        delete_03()
        print("Soluciones creadas.")
    else:
        crear_db()
        print("Ejercicios creados.")