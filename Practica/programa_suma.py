# Programa para sumar tres números y calcular su promedio

try:
    # Pedimos los tres números
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    # Calculamos la suma y el promedio
    suma = num1 + num2 + num3
    promedio = round(suma / 3, 2)

    # Mostramos el resultado usando f-strings
    print(f"La suma de los tres números es: {suma} y su promedio es: {promedio}")

except ValueError:
    print("⚠️ Por favor, ingrese solo números enteros.")


