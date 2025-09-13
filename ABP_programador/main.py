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