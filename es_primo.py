"""
Programa es_primo.py
Autor: Abel García

Decide si un número es primo.

1. Constantes:
    Ninguna.
    
2. Los datos de entrada son:
    x

3. Cálculos:
    a) Para saber si un número x es primo,
        se debe verificar que x no sea múltimo
        de k, con 1 < k < x.

4. Los datos de salida son:
    Verdadero si x es primo y
    Falso en caso contrario.
"""

# Se piden los datos de entrada
print()
x = int(input('Ingresa el número: '))


# Cálculos para saber si el triángulo es equilátero
k = 2
primo = True
while (primo and k <= x/2):
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
