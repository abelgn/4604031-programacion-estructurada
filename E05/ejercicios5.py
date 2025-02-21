

def banner(num):
    print("\n")
    print("***************")
    print("* Ejercicio", num)
    print("***************")




def ejercicio_1():
    banner(1)
    a = float(input("Primer numero: "))
    b = float(input("Segundo numero: "))
    c = float(input("Tercer numero: "))
    
    promedio = (a + b + c) / 3
    print("El promedio de " + str(a) + ", " + str(b) + " y " + str(c) + " es:", promedio)



def ejercicio_2():
    banner(2)
    a = float(input("Precio primer articulo: "))
    b = float(input("Precio segundo articulo: "))
    c = float(input("Precio tercer articulo: "))
    saldo_inical = float(input("Saldo inicial: "))
    
    saldo_final = saldo_inical - (a + b + c)
    print("El saldo final de la tarjeta es:", saldo_final)



def ejercicio_3():
    banner(3)
    tarifa_base = 7
    tarifa_km = 3.57
    tarifa_t = 1.8
    
    d = float(input("Distancia recorrida: "))
    t = float(input("Duracion del viaje: "))
    total = tarifa_base + d * tarifa_km + t * tarifa_t
    
    print("El total a pagar es:", total)


def ejercicio_4():
    banner(4)
    tarifa_base = 199.95
    tarifa_extra = 49.95
    
    articulos = int(input("Cantidad de articulos: "))
    total = tarifa_base + (articulos - 1) * tarifa_extra
    
    print("El total a pagar es:", total)


def ejercicio_5():
    banner(5)
    porcentaje = 4 / 100
    
    saldo = float(input("Saldo inicial: "))
    intereses = saldo * porcentaje
    saldo = saldo + intereses
    print("El saldo al primer año es:", saldo)
    intereses = saldo * porcentaje
    saldo = saldo + intereses
    print("El saldo al segundo año es:", saldo)
    intereses = saldo * porcentaje
    saldo = saldo + intereses
    print("El saldo al tercer año es:", saldo)


def ejercicio_11():
    banner(11)
    
    numero = int(input("Cuál es el número de cuatro dígitos: "))
    suma = numero % 10
    numero = numero // 10
    suma = suma + numero % 10
    numero = numero // 10
    suma = suma + numero % 10
    numero = numero // 10
    suma = suma + numero % 10
    
    print("La suma de los cuatro dígitos es:", suma)


def ejercicio_12():
    banner(12)
    factor_psi = 0.0001450377
    factor_atm = 0.00000986923
    factor_mmhg = 0.00750062
    
    presion = int(input("Cuál es la presión en pascales: "))
    print(presion, "pascales son:")
    print(presion*factor_psi, "libras por pulgada cuadrada")
    print(presion*factor_atm, "atmósferas")
    print(presion*factor_mmhg, "milímetros de mercurio")



#ejercicio_1()

#ejercicio_2()

#ejercicio_3()

#ejercicio_4()

#ejercicio_5()

#ejercicio_11()

ejercicio_12()