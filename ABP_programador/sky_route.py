# ---- config.py ----
# config.py
# Configuración de conexión a la base de datos MySQL

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "tu_contraseña",
    "database": "skyroute_db"
}


# ---- conexion_base_datos.py ----
# conexion_base_datos.py
import mysql.connector
from config import DB_CONFIG

def conectar():
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        return conexion
    except mysql.connector.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None


# ---- gestion_clientes.py ----
# gestion_clientes.py
from conexion_base_datos import conectar

def listar_clientes():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM clientes")
    for cliente in cursor.fetchall():
        print(cliente)
    con.close()


# ---- gestion_destinos.py ----
# gestion_destinos.py
from conexion_base_datos import conectar

def listar_destinos():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM destinos")
    for destino in cursor.fetchall():
        print(destino)
    con.close()


# ---- gestion_ventas.py ----
# gestion_ventas.py
from conexion_base_datos import conectar

def listar_ventas():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ventas")
    for venta in cursor.fetchall():
        print(venta)
    con.close()


# ---- main.py ----
# main.py
from gestion_clientes import listar_clientes
from gestion_destinos import listar_destinos
from gestion_ventas import listar_ventas

def menu():
    while True:
        print("\nSkyRoute - Sistema de Gestión de Pasajes")
        print("1. Listar Clientes")
        print("2. Listar Destinos")
        print("3. Listar Ventas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_clientes()
        elif opcion == "2":
            listar_destinos()
        elif opcion == "3":
            listar_ventas()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()

