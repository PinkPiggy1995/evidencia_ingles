# gestion_clientes.py
from conexion_base_datos import conectar

def listar_clientes():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM clientes")
    for cliente in cursor.fetchall():
        print(cliente)
    con.close()
    