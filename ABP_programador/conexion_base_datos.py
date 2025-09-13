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
    