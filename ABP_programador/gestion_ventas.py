# gestion_ventas.py
from conexion_base_datos import conectar

def listar_ventas():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ventas")
    for venta in cursor.fetchall():
        print(venta)
    con.close()