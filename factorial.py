"""
Programa factorial.py
Autor: Abel García

Calcula el factorial de n.

1. Constantes:
    Ninguna.
    
2. Los datos de entrada son:
    n, el número del cual se quiere calcular el factorial.

3. Cálculos:
    Se calcula la multiplicación 1 x 2 x 3 x ... x (n-1) x n.

4. Los datos de salida son:
    El factorial de n.
"""

from math import sqrt


# Se pide el dato de entrada n
# Se espera que el dato que se ingrese
# sea un número positivo
print()
positivo = False
while not positivo:
    n = input('Ingresa un número positivo: ')
    if n.isdigit() and int(n) > 0:
        positivo = True
n = int(n)


# Calcula el factorial de n
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i


# Se despliega el resultado
print('El factorial de', n, 'es:', factorial)
print()
