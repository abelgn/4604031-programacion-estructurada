"""
Programa figura.py
Autor: Abel García

Dado el número de lados que tiene una figura geométrica, decir qué figura es.

1. Constantes:
    Ninguna.
    
2. Los datos de entrada son:
    el número de lados de la figura

3. Cálculos:
    a) Para saber qué figura es, se deben comparar el número de lados:
            
        3, triángulo
        4, cuadrilátero
        5, pentágono
        6, hexágono
        7, heptágono
        8, octágono
        9, nonágono
        10, decágono

4. Los datos de salida son:
    El nombre de la figura.
"""

# Se piden los datos de entrada
print()
lados = int(input("Cuántos lado tiene la figura: "))


# Se decide qué figura es
if (lados == 3):
    nombre = "triángulo"
elif (lados == 4):
    nombre = "cuadrilátero"
elif (lados == 5):
    nombre = "pentágono"
elif (lados == 6):
    nombre = "hexágono"
elif (lados == 7):
    nombre = "heptágono"
elif (lados == 8):
    nombre = "octágono"
elif (lados == 9):
    nombre = "nonágono"
else:
    nombre = "decágono"


# Se despliega el resultado
print("La figura es un", nombre)
print()
