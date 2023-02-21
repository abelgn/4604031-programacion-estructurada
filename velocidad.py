"""
Programa velocidad.py
Autor: Abel García

Calcula la velocidad final vide un objeto que
golpea el suelo en caída libre, de acuerdo con
la fórmula

vf = RAIZ(vi^2 + 2ad)       (1)

en donde vi es la velocidad inicial, a es la
aceleración y d es la distancia.

1. Constantes:
    la aceleración de la gravedad
    a = 9.8 m/s^2
    vi = 0 m/s
    
2. Los datos de entrada son:
    distancia

3. Cálculos:
    Se calcula la velocidad final de acuerdo
    con la fórmula (1).

4. Los datos de salida son:
    la velocidad final del objeto al golpear
    el suelo.
"""

import math

# Inicialización la constante de los gases ideales
aceleracion = 9.8
vi = 0.0


# Se piden los datos de entrada
print()
distancia = float(input("Introduce la distancia: "))


# Cáclulos para la velocidad final
vf = math.sqrt(vi**2 + 2.0 * aceleracion * distancia)


# Se despliega el resultado
print("La velocidad final es ", vf, "m/s")
print()
