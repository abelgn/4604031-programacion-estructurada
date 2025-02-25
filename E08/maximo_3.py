"""
Programa maximo_3.py
Autor: Abel García

Decide cuál de tres números, a, b o c, es el máximo.

1. Constantes:
    Ninguna.
    
2. Los datos de entrada son:
    número a
    número b
    número c

3. Cálculos:
    a) Para saber cuál de los tres números es el
    máximo, se deben comparar entre ellos:
            
            a >= b y a >= c
            b >= a y b >= c

4. Los datos de salida son:
    El máximo de los tres números a, b y c.
"""

# Se piden los datos de entrada
print()
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))


# Se decide cuál de los dos números es el máximo
if a >= b:
    if a >= c:
        maximo = a
    else:
        maximo = c
else:
    if b >= c:
        maximo = b
    else:
        maximo = c


# Se despliega el resultado
print('El máximo es', maximo)
print()
