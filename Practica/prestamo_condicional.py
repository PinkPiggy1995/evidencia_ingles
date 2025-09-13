###
# Prestamo de un banco: Desarrollar un programa en Python, que verifique la edad de una persona e 
# indique si es posible otorgarle un prestamo persona. Las condiciones para hacerlo son: 
#a) Sea mayor de edad
# b) sea menor de 65 años
# En caso contrario no será posible otorgar el préstamo. 



edad = int(input("Ingrese la edad de la persona: "))

if edad >= 18 and edad < 65:
    print("Felicitaciones, puede acceder al crédito")

else:
    print("En este momento no cuenta con prestamos disponibles")



