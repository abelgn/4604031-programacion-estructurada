"""
Programa es_primo.py
Autor: Abel García

Decide si un número es primo.

Un número > 1 es primo si únicamente es
divisible entre 1 y él mismo.

1. Constantes:
    Ninguna.
    
2. Los datos de entrada son:
    x, el número entero positivo a verificar
    si es primo.

3. Cálculos:
    a) Para saber si un número x es primo,
        se debe verificar que x no es múltiplo
        de k, con 1 < k < x.

4. Los datos de salida son:
    Verdadero si x es primo y
    Falso en caso contrario.
"""

from math import sqrt


# Se piden el dato de entrada
# Se espera que el dato que se ingrese
# sea un número positivo mayor que 1
print()
positivo = False
while not positivo:
    x = input('Ingresa un número mayor que 1: ')
    if x.isdigit() and int(x) > 1:
        positivo = True
x = int(x)


# Verificación para saber si x es primo
k = 2
primo = True
while primo and k <= sqrt(x):
    if x % k == 0:
        primo = False
    k = k + 1


# Se decide si el número es primo
if primo:
    resp = 'es número primo'
else:
    resp = 'no es número primo'


# Se despliega el resultado
print(x, resp)
print()
