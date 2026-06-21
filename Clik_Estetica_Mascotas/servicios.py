# =========================
# servicios.py
# =========================

from database import conn, cursor
from datetime import datetime
import csv


# REGISTRAR SERVICIO
# REGISTRAR SERVICIO

# VER HISTORIAL GENERAL
def ver_historial():

    cursor.execute("""
        SELECT mascotas.nombre,
               servicios.servicio,
               servicios.precio,
               servicios.fecha
        FROM servicios
        JOIN mascotas
        ON mascotas.id = servicios.mascota_id
        ORDER BY servicios.fecha DESC
    """)

    datos = cursor.fetchall()

    if not datos:
        print("No hay servicios registrados")
        return

    print("\nHISTORIAL GENERAL\n")

    for d in datos:
        print(f"Mascota: {d[0]}")
        print(f"Servicio: {d[1]}")
        print(f"Precio: S/ {d[2]:.2f}")
        print(f"Fecha: {d[3]}")
        print("----------------")
# REGISTRAR SERVICIO
def registrar_servicio():

    try:
        mascota_id = int(input("ID de mascota: "))

    except ValueError:
        print("ID invalido")
        return


    # BUSCAR MASCOTA
    cursor.execute("""
        SELECT nombre, raza
        FROM mascotas
        WHERE id = ?
    """, (mascota_id,))

    mascota = cursor.fetchone()

    if mascota is None:
        print("La mascota no existe")
        return


    nombre_mascota = mascota[0]
    raza_mascota = mascota[1]


    print(f"\nMascota seleccionada: {nombre_mascota}")
    print(f"Raza: {raza_mascota}")


    # MENU PRINCIPAL
    print("""
=============================
        SERVICIOS
=============================

1. Tintura de cabello
2. Peluqueria
3. Brillo para el cabello
4. Baño de color o brillo
5. Cortes
6. Renacimiento capilar
7. Cepillado de dientes
8. Colorimetria
9. Baño y corte de pelo por raza
10. Limpieza de glandulas anales
11. Corte de uñas
12. Consultorio estetico
""")

    opcion_servicio = input("Seleccione un servicio: ").strip()


    # =========================
    # SERVICIO NORMAL
    # =========================
    servicios = {
        "1": "Tintura de cabello",
        "2": "Peluqueria",
        "3": "Brillo para el cabello",
        "4": "Baño de color o brillo",
        "5": "Cortes",
        "6": "Renacimiento capilar",
        "7": "Cepillado de dientes",
        "8": "Colorimetria",
        "10": "Limpieza de glandulas anales",
        "11": "Corte de uñas",
        "12": "Consultorio estetico"
    }
    precios = {
    "Tintura de cabello": 80.0,
    "Peluqueria": 50.0,
    "Brillo para el cabello": 40.0,
    "Baño de color o brillo": 60.0,
    "Cortes": 45.0,
    "Renacimiento capilar": 90.0,
    "Cepillado de dientes": 30.0,
    "Colorimetria": 70.0,
    "Limpieza de glandulas anales": 35.0,
    "Corte de uñas": 20.0,
    "Consultorio estetico": 100.0
    }


    # =========================
    # CORTES POR RAZA
    # =========================
    if opcion_servicio == "9":

        # MENUS SEGUN RAZA
        cortes_por_raza = {

            "Pitbull": {
                "1": "Corte militar",
                "2": "Corte americano",
                "3": "Corte brillante corto"
            },

            "Poodle": {
                "1": "Corte continental",
                "2": "Corte cachorro",
                "3": "Corte teddy bear"
            },

            "Husky": {
                "1": "Cepillado nordico",
                "2": "Deslanado completo",
                "3": "Baño premium husky"
            },

            "Labrador": {
                "1": "Cepillado clasico",
                "2": "Baño brillante",
                "3": "Deslanado suave"
            },

            "Bulldog": {
                "1": "Limpieza facial",
                "2": "Baño dermatologico",
                "3": "Cepillado corto"
            },

            "Chihuahua": {
                "1": "Corte mini",
                "2": "Corte elegante",
                "3": "Baño premium pequeño"
            },

            "Golden Retriever": {
                "1": "Corte pluma",
                "2": "Deslanado golden",
                "3": "Cepillado premium"
            },

            "Pastor Aleman": {
                "1": "Deslanado aleman",
                "2": "Cepillado intenso",
                "3": "Baño protector"
            },

            "Siamés": {
                "1": "Cepillado felino",
                "2": "Baño delicado",
                "3": "Limpieza premium"
            },

            "Persa": {
                "1": "Corte león",
                "2": "Cepillado persa",
                "3": "Desenredado completo"
            }
        }


        # VERIFICAR SI EXISTE ESA RAZA
        if raza_mascota not in cortes_por_raza:

            print("No hay cortes registrados para esta raza")
            return


        print(f"\nCORTES PARA {raza_mascota.upper()}\n")


        # MOSTRAR MENU AUTOMATICO
        for clave, corte in cortes_por_raza[raza_mascota].items():

            print(f"{clave}. {corte}")


        opcion_corte = input("\nSeleccione un corte: ").strip()


        if opcion_corte not in cortes_por_raza[raza_mascota]:

            print("Opcion invalida")
            return


        corte_elegido = cortes_por_raza[raza_mascota][opcion_corte]

        servicio = f"Corte para {raza_mascota}: {corte_elegido}"
        
        precios_cortes = {
            "Pitbull": 70.0,
            "Poodle": 90.0,
            "Husky": 110.0,
            "Labrador": 80.0,
            "Bulldog": 75.0,
            "Chihuahua": 60.0,
            "Golden Retriever": 100.0,
            "Pastor Aleman": 95.0,
            "Siamés": 55.0,
            "Persa": 85.0
        }

        precio = precios_cortes[raza_mascota]


    # =========================
    # SERVICIO NORMAL
    # =========================
    elif opcion_servicio in servicios:

        servicio = servicios[opcion_servicio]
        precio = precios[servicio]


    else:
        print("Opcion invalida")
        return

    
    print(f"\nServicio seleccionado: {servicio}")
    print(f"Precio: S/ {precio:.2f}")

    while True:
        
        fecha = input("Fecha (YYYY-MM-DD): ").strip()
        
        try:
            
            fecha_ingresada = datetime.strptime(
            fecha,
            "%Y-%m-%d"
        ).date()
            
            fecha_actual = datetime.now().date()
            
            if fecha_ingresada < fecha_actual:
                print("No se permiten fechas pasadas")
                continue
            
            if fecha_ingresada.year > fecha_actual.year + 1:
                print("La fecha es demasiado lejana")
                continue
            
            break
        except ValueError:
            print("Fecha invalida")


    # INSERTAR SERVICIO
    cursor.execute("""
        INSERT INTO servicios
        (mascota_id, servicio, precio, fecha)
        VALUES (?, ?, ?, ?)
    """, (
        mascota_id,
        servicio,
        precio,
        fecha
    ))

    conn.commit()

    print("Servicio registrado correctamente")


# VER HISTORIAL POR DNI
def ver_historial_mascota():

    dni = input("DNI del propietario: ").strip()

    if not dni.isdigit():
        print("El DNI solo debe contener numeros")
        return


    cursor.execute("""
        SELECT mascotas.nombre,
               servicios.servicio,
               servicios.precio,
               servicios.fecha,
               mascotas.propietario,
               mascotas.dni
        FROM servicios
        JOIN mascotas
        ON mascotas.id = servicios.mascota_id
        WHERE mascotas.dni = ?
        ORDER BY servicios.fecha DESC
    """, (dni,))

    datos = cursor.fetchall()

    if not datos:
        print("No hay historial para ese DNI")
        return


    print("\nHISTORIAL DE MASCOTAS\n")

    print(f"Propietario: {datos[0][4]}")
    print(f"DNI: {datos[0][5]}\n")

    for d in datos:

        print(f"Mascota: {d[0]}")
        print(f"Servicio: {d[1]}")
        print(f"Precio: S/ {d[2]:.2f}")
        print(f"Fecha: {d[3]}")
        print("----------------")

def crear_corte_personalizado(raza):
    print(f"\nAñadir corte personalizado para {raza}\n")

    nombre = input("Nombre del corte: ").strip().title()

    if not nombre:
        print("Nombre inválido")
        return None

    while True:
        try:
            precio = float(input("Precio del corte: S/ "))
            if precio <= 0:
                print("Precio inválido")
                continue
            break
        except ValueError:
            print("Número inválido")

    confirmar = input(f"""
Nombre: {nombre}
Precio: {precio}
Confirmar (S/N): """).strip().upper()

    if confirmar != "S":
        print("Cancelado")
        return None

    cursor.execute("""
        INSERT INTO cortes_personalizados (raza, nombre_corte, precio)
        VALUES (?, ?, ?)
    """, (raza, nombre, precio))

    conn.commit()

    print("Corte guardado correctamente")

    return nombre, precio

