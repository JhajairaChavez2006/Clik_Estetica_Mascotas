# =========================
# exportaciones.py
# =========================

from database import cursor
import csv


def exportar_csv():

    # EXPORTAR MASCOTAS
    cursor.execute("SELECT * FROM mascotas")
    mascotas = cursor.fetchall()

    with open("mascotas.csv", "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "id",
            "nombre",
            "especie",
            "raza",
            "edad",
            "propietario",
            "dni"
        ])

        writer.writerows(mascotas)


    # EXPORTAR SERVICIOS
    cursor.execute("SELECT * FROM servicios")
    servicios = cursor.fetchall()

    with open("servicios.csv", "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "id",
            "mascota_id",
            "servicio",
            "precio",
            "fecha"
        ])

        writer.writerows(servicios)

    print("Exportacion completada")