2028"""
Programa bisiesto.py
Autor: Abel García

Decide si un año es bisiesto, considerando que un
año es bisiesto si se cumple una de las siguientes
reglas:

a) El año es múltiplo de cuatro, pero no de 100.
b) El año es múltiplo de 400.

1. Constantes:
    Ninguna.
    
2. Los datos de entrada son:
    año

3. Cálculos:
    a) Para saber si el año es múltiplo de 4,
        pero no de 100, se calcula la división
        entera año/4 y año/100. El residuo de
        la primera división debe ser cero y el
        de la segunda NO debe ser cero.
        
    b) Para saber si el año es múltiplo de 400,
        se calcula la división entera año/400.
        El residuo de la división debe ser cero.

4. Los datos de salida son:
    Verdadero si el año es bisiesto y Falso en
    caso contrario.
"""

# Se piden los datos de entrada
print()
anio = int(input("Introduce el año: "))


# Cálculos para saber si el año es bisiesto
# Múltiplo de 4 pero no de 100
bis1 = (anio % 4 == 0) and (anio % 100 != 0)

# Múltiplo de 400
bis2 = anio % 400 == 0


# Se decide si año es bisiesto cuando se cumple
# alguna de las dos reglas anteriores
if bis1 or bis2:
    resp = 'es bisiesto'
else:
    resp = 'no es bisiesto'


# Se despliega el resultado
print(anio, resp)
print()
