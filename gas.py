"""
Programa gas.py
Autor: Abel García

Calcula la cantidad de gas en moles utilizando la
ley de los gases ideales:

PV = nRT (1)

en donde P es la presión en pascales, V el volumen
en litros, n la cantidad de gas en moles, R es la
constante de los gases ideales y T es la temperatura
en Kelvin.

1. Constantes:
    la constante de los gases ideales
    R = 8.314 J / (mol K)
    
2. Los datos de entrada son:
    presión
    volumen
    temperatura

3. Cálculos:
    Se calcula la cantidad de gas en moles despejando
    a n de la fórmula (1)
    
         P V
    n = -----
         R T

4. Los datos de salida son:
    la cantidad de gas en moles
"""


# Inicialización la constante de los gases ideales
R = 8.314


# Se piden los datos de entrada
print()
presion = float(input("Introduce la presión: "))
volumen = float(input("Introduce el volumen: "))
temperatura = float(input("Introduce la temperatura: "))


# Cáclulo de la cantidad de gas
moles = (presion * volumen) / (R * temperatura)


# Se despliega el resultado
print("La cantidad de gas es ", moles, "moles")
print()
