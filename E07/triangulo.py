"""
Programa triangulo.py
Autor: Abel García

Dadas las longitudes de los tres lados de un 
triángulo, decide qué tipo de triángulo es.

1. Constantes:
    Ninguna.
    
2. Los datos de entrada son:
    lado a
    lado b
    lado c

3. Cálculos:
    a) Para saber qué tipo de triángulo es, se deben comparar las longitudes entre ellas:
            
            a == b y b == c, equilátero
            a != b y a != c y b != c, escaleno

4. Los datos de salida son:
    El tipo de triángulo.
"""

# Se piden los datos de entrada
print()
a = float(input("Longitud primer lado: "))
b = float(input("Longitud segundo lado: "))
c = float(input("Longitud tercer lado: "))


# Se decide qué tipo de triángulo es
if a == b and b >= c:
    tipo = "equilátero"
elif a != b and a != c and b != c:
    tipo = "escaleno"
else:
    tipo = "isósceles"


# Se despliega el resultado
print("El triángulo es", tipo)
print()
