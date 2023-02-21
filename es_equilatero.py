"""
Programa es_equilatero.py
Autor: Abel García

Decide si un triángulo es equilátero, dadas las
longitudes de sus lados. Un triángulo es
equilátero si sus tres lados tienen la misma
longitud.

1. Constantes:
    Ninguna.
    
2. Los datos de entrada son:
    lado a
    lado b
    lado c

3. Cálculos:
    a) Para saber si un triángulo es equiátero,
        se deben comparar las longitudes de sus
        lados y deben ser las mismas:
            
            (a = b) Y (b = c)

4. Los datos de salida son:
    Verdadero si el triángulo es equilátero y
    Falso en caso contrario.
"""

# Se piden los datos de entrada
print()
a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))


# Cáclulos para saber si el triángulo es equilátero
es_quilatero = (a == b) and (b == c)


# Se decide si el triángulo es equilatero cuando se
# cumple la condición anterior
if es_quilatero:
    resp = 'es equilátero'
else:
    resp = 'no es equilátero'


# Se despliega el resultado
print('El triángulo', resp)
print()
