#Un hincha de fútbol desea conocer la cantidad de puntos que su equipo lleva acumulados en el 
# campeonato, para ello recibe cada semana la información de la cantidad total de partidos, desde el 
# inicio del campeonato, que el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado
# recibe un punto, por cada partido ganado tres puntos y por los perdidos cero puntos.

partidos_g = int(input("Ingrese la cantidad de partidos ganados: "))
partidos_e = int(input("Ingrese la cantidad de partidos empatados: "))
partidos_p = int(input("Ingrese la cantidad de partidos perdidos: "))

puntos_g = partidos_g * 3
puntos_e = partidos_e * 1
puntos_p = partidos_p * 0

total_puntos = puntos_g + puntos_e + puntos_p

print ("El total de puntos que sumo su equipo es de: ", total_puntos)
