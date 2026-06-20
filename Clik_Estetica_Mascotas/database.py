# =========================
# database.py
# =========================

import sqlite3

conn = sqlite3.connect("spa_click.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


def crear_tablas():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mascotas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        especie TEXT NOT NULL,
        raza TEXT NOT NULL,
        edad TEXT NOT NULL,
        propietario TEXT NOT NULL,
        dni TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS servicios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mascota_id INTEGER NOT NULL,
    servicio TEXT NOT NULL,
    precio REAL NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (mascota_id)
        REFERENCES mascotas(id)
        ON DELETE CASCADE
    )
    """)
    
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS razas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cortes_personalizados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    raza TEXT NOT NULL,
    nombre_corte TEXT NOT NULL,
    precio REAL NOT NULL
    )
    """)

    conn.commit()