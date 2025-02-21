"""
Programa maximo_2.py
Autor: Abel García

Decide cuál de dos números, a o b, es el máximo.

1. Constantes:
    Ninguna.
    
2. Los datos de entrada son:
    número a
    número b

3. Cálculos:
    a) Para saber cuál de los dos números es el
    máximo, se deben comparar entre ellos:
            
            a >= b

4. Los datos de salida son:
    El máximo de los dos números a y b.
"""

# Se piden los datos de entrada
print()
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))


# Se decide cuál de los dos números es el máximo
if a >= b:
    maximo = a
else:
    maximo = b


# Se despliega el resultado
print('El máximo es', maximo)
print()
