# CLIK – Sistema de Gestión de Mascotas

## Descripción del programa

CLIK es un sistema de gestión por consola para Mascot Spa CLIK, un negocio de estética para mascotas ubicado en Cajamarca, Perú. El programa digitaliza el registro de mascotas, propietarios y servicios estéticos, reemplazando el uso de fichas físicas por un proceso centralizado, validado y con historial consultable en segundos.

El sistema permite registrar mascotas y sus propietarios, buscar y modificar esa información, asociar servicios estéticos con su precio y fecha, consultar historiales de atención (general o por propietario) y exportar todos los datos a archivos CSV como respaldo.

## Contexto del proyecto

Proyecto final del curso Fundamentos de Programación (CIIN1205P) — Ingeniería de Sistemas Computacionales.

**Problema:** ineficiencia en el proceso de atención y seguimiento de servicios estéticos para mascotas.

**Solución elegida:** sistema de gestión en Python con interfaz de consola y base de datos SQLite (ver comparación de alternativas en el informe del proyecto).

## Lenguaje y tecnologías

- **Lenguaje:** Python 3
- **Base de datos:** SQLite 3 (archivo local spa_click.db)
- **Persistencia secundaria:** exportación a archivos CSV

## Dependencias

El programa no requiere librerías externas. Utiliza únicamente módulos de la biblioteca estándar de Python:

- sqlite3 — conexión y manejo de la base de datos
- csv — exportación de datos a archivos .csv
- datetime — validación de fechas de servicios

**Requisito de entorno:** Python 3.8 o superior instalado en el equipo.

## Funcionalidades

| # | Función | Descripción |
|---|---------|-------------|
| 1 | Registrar mascota | Captura nombre, especie, raza, edad, propietario y DNI, con validaciones. |
| 2 | Ver mascotas (A-Z) | Lista todas las mascotas ordenadas alfabéticamente. |
| 3 | Buscar mascota | Búsqueda por nombre o por DNI del propietario. |
| 4 | Modificar mascota | Actualiza los datos de una mascota existente por ID. |
| 5 | Eliminar mascota | Elimina una mascota y sus servicios asociados (en cascada), con confirmación. |
| 6 | Registrar servicio | Asocia un servicio estético (de catálogo o por raza) a una mascota, con precio y fecha. |
| 7 | Ver historial general | Muestra todos los servicios registrados, ordenados por fecha. |
| 8 | Ver historial por DNI | Filtra el historial de servicios según el DNI del propietario. |
| 9 | Exportar a CSV | Genera mascotas.csv y servicios.csv como respaldo. |
| 10 | Salir | Cierra la conexión a la base de datos y termina el programa. |

## Estructura del proyecto

```
CLIK_Estetico_Mascotas/
├── main.py            # Punto de entrada: menú principal y bucle del sistema
├── database.py        # Conexión a SQLite y creación de tablas
├── mascotas.py         # CRUD de mascotas (registrar, ver, buscar, modificar, eliminar)
├── servicios.py        # Registro de servicios, catálogo de precios e historiales
├── exportaciones.py    # Exportación de datos a archivos CSV
└── spa_click.db         # Base de datos SQLite (se genera al ejecutar el programa)
```

### Tablas de la base de datos

- **mascotas**: id, nombre, especie, raza, edad, propietario, dni
- **servicios**: id, mascota_id (FK → mascotas.id, ON DELETE CASCADE), servicio, precio, fecha
- **razas**: id, nombre — razas personalizadas registradas por el usuario
- **cortes_personalizados**: id, raza, nombre_corte, precio — cortes adicionales por raza

## Instalación y ejecución

Clonar o descargar el repositorio:
   ```bash
   git clone https://github.com/JhajairaChavez2006/Clik_Estetica_Mascotas.git
   cd Clik_Estetica_Mascotas
   ```

## Uso

Al iniciar, el sistema muestra el menú principal:

```
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
```

Se ingresa el número de la opción deseada y se sigue las indicaciones en pantalla. El programa valida cada dato ingresado (nombre, edad, DNI, fecha, etc.) y solicita corrección en caso de error, sin cerrar la ejecución.

### Validaciones principales

- **Nombre / propietario:** solo letras y espacios, longitud mínima.
- **Edad:** años entre 0 y 30, meses entre 0 y 11.
- **DNI:** solo números, entre 8 y 9 dígitos.
- **Fecha de servicio:** formato AAAA-MM-DD, no anterior a hoy ni a más de un año en el futuro.
- **Eliminación:** requiere confirmación explícita (S/N) antes de borrar.

## Exportación de datos

La opción 9. Exportar CSV genera dos archivos en el directorio del proyecto:

- mascotas.csv — todos los registros de la tabla mascotas
- servicios.csv — todos los registros de la tabla servicios

## Autores

Proyecto desarrollado por el Equipo 1:

- Chávez Díaz, Jhajaira Roxana
- Portal Carrión, Mariela
- Sáenz Veliz, Amir Imanol
- Vásquez Valdez, Jaime Farid
- Villegas Guevara, Luis Adrián
