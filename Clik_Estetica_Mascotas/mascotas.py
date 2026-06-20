# =========================
# mascotas.py
# =========================

from database import conn, cursor
from servicios import crear_corte_personalizado


# REGISTRAR MASCOTA
# REGISTRAR MASCOTA
def registrar_mascota():

    while True:

        nombre = input("Nombre: ").strip()

        # SOLO LETRAS Y ESPACIOS
        if not nombre.replace(" ", "").isalpha():
            print("Los caracteres son invalidos")
            continue

        if len(nombre) < 2 or len(nombre) > 20:
            print("Nombre invalido (Demasiados caracteres)")
            continue

        break
    # ESPECIE Y RAZA
    while True:

        print("""
    Seleccione la especie:

    1. Perro
    2. Gato
    """)

        opcion_especie = input("Opcion: ").strip()


    # =========================
    # PERROS
    # =========================
        if opcion_especie == "1":

            especie = "Perro"

            print("""
    Seleccione una raza:

    1. Labrador
    2. Pastor Aleman
    3. Bulldog
    4. Poodle
    5. Golden Retriever
    6. Chihuahua
    7. Pitbull
    8. Husky
    9. Otra raza
    """)

            opcion_raza = input("Opcion: ").strip()

            razas_perros = {
                "1": "Labrador",
                "2": "Pastor Aleman",
                "3": "Bulldog",
                "4": "Poodle",
                "5": "Golden Retriever",
                "6": "Chihuahua",
                "7": "Pitbull",
                "8": "Husky",
                "9": "Otra raza"
            }

            if opcion_raza in razas_perros:
                
                if opcion_raza == "9":
                     raza = input("Ingrese la raza: ").strip().title()
                     
                     if not raza.replace(" ", "").isalpha():
                         print("La raza solo puede contener letras")
                         continue
                     if len(raza) < 3:
                         print("Raza")
                         continue
                     confirmar = input(f"¿La raza '{raza}' es correcta? (S/N): ").strip().upper()
                     
                     if confirmar != "S":
                            continue
                        # GUARDAR RAZA
                     cursor.execute("""
                         INSERT OR IGNORE INTO razas(nombre)
                         VALUES (?)
                     """, (raza,))
                     
                     conn.commit
                     
                     
                     
                    
                   
                            
                      
                            
                            
                            
                            

                else:       

                    raza = razas_perros[opcion_raza]

            else:
                print("Opcion invalida")
                continue

            break


    # =========================
    # GATOS
    # =========================
        elif opcion_especie == "2":

            especie = "Gato"

            print("""
            Seleccione una raza:

            1. Siamés
            2. Persa
            3. Bengalí
            4. Maine Coon
            5. Azul Ruso
            6. Sphynx
            7. Angora
            8. Británico
            9. Otra raza
            """)

            opcion_raza = input("Opcion: ").strip()

            razas_gatos = {
                "1": "Siamés",
                "2": "Persa",
                "3": "Bengalí",
                "4": "Maine Coon",
                "5": "Azul Ruso",
                "6": "Sphynx",
                "7": "Angora",
                "8": "Británico",
                "9": "Otra raza"
            }


            if opcion_raza in razas_gatos:
                
                if opcion_raza == "9":
                    
                    while True:
                        
                        raza = input(
                            "Ingrese la raza: "
                        ).strip().title()
                        
                        if not raza.replace(" ", "").isalpha():
                            print(
                                "La raza solo puede contener letras"
                            )
                            continue
                        
                        if len(raza) < 3:
                            print("Raza invalida")
                            continue
                        
                        confirmar = input(
                            f"¿La raza '{raza}' es correcta? (S/N): "
                        ).strip().upper()
                        
                        if confirmar == "S":
                            raza = input("Ingrese la raza: ").strip().title()
                            
                            
                            if not raza.replace(" ", "").isalpha():
                                print("La raza solo puede contener letras")
                                continue
                            
                            if len(raza) < 3:
                                print("Raza invalida")
                                continue
                            
                            confirmar = input(f"¿La raza '{raza}' es correcta? (S/N): ").strip().upper()
                            
                            if confirmar != "S":
                                continue
                             # GUARDAR RAZA
                            cursor.execute("""
                                INSERT OR IGNORE INTO razas(nombre)
                                VALUES (?)
                            """, (raza,))
                            conn.commit
                    
                     
                            break
                            
                            
                                    
                            

                else:
                    raza = razas_gatos[opcion_raza]

            else:
                print("Opcion invalida")
                continue

            break
        
        else:
            print("Opcion invalida")

    # EDAD
    while True:

        try:
            años = int(input("Edad (años): "))
            meses = int(input("Meses adicionales: "))

            if años < 0:
                print("Los años no pueden ser negativos")
                continue

            if años > 30:
                print("Edad invalida")
                continue

            if meses < 0 or meses > 11:
                print("Los meses deben estar entre 0 y 11")
                continue

            edad = f"{años} años y {meses} meses"

            break

        except ValueError:
            print("Ingrese numeros enteros")


    # PROPIETARIO
    while True:

        propietario = input("Propietario: ").strip()

        if not propietario.replace(" ", "").isalpha():
            print("El propietario solo debe contener letras")
            continue

        if len(propietario) < 3:
            print("Propietario invalido")
            continue

        break


    # DNI
    while True:

        dni = input("DNI del propietario: ").strip()

        if not dni.isdigit():
            print("El DNI solo debe contener numeros")
            continue

        if len(dni) < 8 or len(dni) > 9:
            print("El DNI debe tener entre 8 y 9 digitos")
            continue

        break


    cursor.execute("""
        INSERT INTO mascotas
        (nombre, especie, raza, edad, propietario, dni)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        nombre,
        especie,
        raza,
        edad,
        propietario,
        dni
    ))

    conn.commit()

    print("Mascota registrada correctamente")
    
# VER MASCOTAS ORDENADAS ALFABETICAMENTE
def ver_mascotas():

    cursor.execute("""
        SELECT * FROM mascotas
        ORDER BY nombre COLLATE NOCASE ASC
    """)

    mascotas = cursor.fetchall()

    if not mascotas:
        print("No hay mascotas registradas")
        return


    print("\nLISTA DE MASCOTAS\n")

    for m in mascotas:

        print(f"ID: {m[0]}")
        print(f"Nombre: {m[1]}")
        print(f"Especie: {m[2]}")
        print(f"Raza: {m[3]}")
        print(f"Edad: {m[4]}")
        print(f"Propietario: {m[5]}")
        print(f"DNI: {m[6]}")
        print("----------------------")
        
# BUSCAR MASCOTA POR NOMBRE O DNI
def buscar_mascota():

    print("""
1. Buscar por nombre
2. Buscar por DNI
""")

    opcion = input("Opcion: ").strip()


    # BUSCAR POR NOMBRE
    if opcion == "1":

        nombre = input("Nombre a buscar: ").strip()

        if not nombre:
            print("Debe ingresar un nombre")
            return

        # SOLO LETRAS Y ESPACIOS
        if not nombre.replace(" ", "").isalpha():
            print("Ingrese solo letras")
            return


        cursor.execute("""
            SELECT * FROM mascotas
            WHERE nombre LIKE ?
        """, (f"%{nombre}%",))

        resultados = cursor.fetchall()

        if not resultados:
            print("No se encontraron mascotas")
            return


        print("\nMASCOTAS ENCONTRADAS\n")

        for r in resultados:

            print(f"ID: {r[0]}")
            print(f"Nombre: {r[1]}")
            print(f"Especie: {r[2]}")
            print(f"Raza: {r[3]}")
            print(f"Edad: {r[4]}")
            print(f"Propietario: {r[5]}")
            print(f"DNI: {r[6]}")
            print("----------------------")


    # BUSCAR POR DNI
    elif opcion == "2":

        dni = input("DNI del propietario: ").strip()

        if not dni.isdigit():
            print("El DNI solo debe contener numeros")
            return

        if len(dni) < 8 or len(dni) > 9:
            print("El DNI debe tener entre 8 y 9 digitos")
            return


        cursor.execute("""
            SELECT * FROM mascotas
            WHERE dni = ?
        """, (dni,))

        resultados = cursor.fetchall()

        if not resultados:
            print("No se encontraron mascotas")
            return


        print("\nMASCOTAS ENCONTRADAS\n")

        for r in resultados:

            print(f"ID: {r[0]}")
            print(f"Nombre: {r[1]}")
            print(f"Especie: {r[2]}")
            print(f"Raza: {r[3]}")
            print(f"Edad: {r[4]}")
            print(f"Propietario: {r[5]}")
            print(f"DNI: {r[6]}")
            print("----------------------")


    else:
        print("Opcion invalida")
