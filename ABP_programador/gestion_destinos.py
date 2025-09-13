# gestion_destinos.py
from conexion_base_datos import conectar

def listar_destinos():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM destinos")
    for destino in cursor.fetchall():
        print(destino)
    con.close()
    