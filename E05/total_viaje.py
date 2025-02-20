print("\n")
print("***************")
print("* Ejercicio 3")
print("***************")

tarifa_base = 7
tarifa_km = 3.57
tarifa_t = 1.8
distancia = float(input("Distancia recorrida: "))
tiempo = float(input("Duración del viaje: "))
total = tarifa_base + distancia * tarifa_km + tiempo * tarifa_t
print("El total a pagar es:", total, "\n\n\n")
