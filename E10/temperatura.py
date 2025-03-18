"""
Programa temperatura.py
Autor: Abel García

Muestra la temperatura en grados Celsius y su correspondiente
conversión a grados Fahrenheit. La conversión incluye todas
las temperaturas entre 0 y 100 grados Celsius que son
múltiplos de 10.

1. Constantes:
    Ninguna.
    
2. Los datos de entrada son:
    Ninguno.

3. Cálculos:
    La fórmula para convertir grados Celsius (C) a grados
    Fahrenheit (F) es
    
    F = (C x 9/5) + 32.

4. Los datos de salida son:
    Los grados Celsius y su correspondiente en grados Fahrenheit.
"""


print()
print("Celsius\tFahrenheit")

# Calcula el factorial de n
for i in range(0, 101, 10):
    celsius = i
    fahrenheit = (celsius * 9.0/5) + 32

    # Se despliega el resultado
    print("%3d\t\t%3d" % (celsius, int(fahrenheit)))

print()
