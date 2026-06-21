# Importa la función para crear tablas y la conexión a la base de datos
from database import crear_tablas, conn

# Importa funciones relacionadas con mascotas
from mascotas import (
    registrar_mascota,      # Agrega una nueva mascota
    ver_mascotas,           # Muestra todas las mascotas ordenadas
    buscar_mascota,         # Busca una mascota específica
    modificar_mascota,      # Edita datos de una mascota
    eliminar_mascota        # Elimina una mascota
)

# Importa funciones relacionadas con servicios
from servicios import (
    registrar_servicio,     # Registra un servicio 
    ver_historial,          # Muestra todo el historial de servicios
    ver_historial_mascota   # Muestra historial por mascota o DNI
)

# Importa función para exportar datos a CSV
from exportaciones import exportar_csv


# Crea las tablas necesarias en la base de datos (si no existen)
crear_tablas()


# Bucle (menú CLIk)
while True:

    # Menú de opciones
    print("""
=============================
        SPA CLIK
=============================
1. Registrar mascota
2. Ver mascotas (A-Z)
3. Buscar mascota
4. Modificar mascota
5. Eliminar mascota
6. Registrar servicio
7. Ver historial general
8. Ver historial por DNI
9. Exportar CSV
10. Salir
""")

    # Captura la opción del usuario
    op = input("Opcion: ").strip()
    #=======Se llaman a las funciones=========
    # Opción 1: Registrar mascota
    if op == "1":
        registrar_mascota()

    # Opción 2: Ver lista de mascotas
    elif op == "2":
        ver_mascotas()

    # Opción 3: Buscar mascota específica
    elif op == "3":
        buscar_mascota()

    # Opción 4: Modificar datos de una mascota
    elif op == "4":
        modificar_mascota()

    # Opción 5: Eliminar mascota
    elif op == "5":
        eliminar_mascota()

    # Opción 6: Registrar un servicio para una mascota
    elif op == "6":
        registrar_servicio()

    # Opción 7: Ver historial completo de servicios
    elif op == "7":
        ver_historial()

    # Opción 8: Ver historial filtrado por DNI o mascota
    elif op == "8":
        ver_historial_mascota()

    # Opción 9: Exportar datos a archivo CSV
    elif op == "9":
        exportar_csv()

    # Opción 10: Salir del programa
    elif op == "10":
        print("Saliendo...")
        break

    # Opción inválida
    else:
        print("Opcion invalida")


# Cierra la conexión a la base de datos al salir del programa
conn.close()