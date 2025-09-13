## realizar un programa en Python que consulte el día de la semana en el que se está 
# e imprimir el mensaje "Feliz fin de semana", si el día es Sábado o Domingo. 
# En el caso que sea otro día indicar que se debe ir al colegio o estudiar. 

dia = input("Ingrese el día de la semana en el que se está: ")

if dia == "sabado" or dia == "domingo": 
    print("Feliz fin de semana")
else:
    print("Zapatero a tus zapatos")
