"""
Programa palindromo.py
Autor: Abel García

Para que una secuencia de letras sea un palíndromo,
esta secuencia se tiene que leer igual de izquiera
a derecha que de derecha a izquierda.
Verifica si una secuencia de letras es un palíndromo

1. Constantes:
    Ninguna.
    
2. Los datos de entrada son:
    Una secuencia de n letras.

3. Cálculos:
    Se tiene que cumplir que el orden de las letras
    de izquierda a derecha sea el mismo que de derecha
    a izquierda.

4. Los datos de salida son:
    Indicar si la secuencia de letras es un palíndromo.
"""


# Se pide la secuencia de n letras.
# Se espera que la secuencia solo contenga letras.
print()
solo_letras = False
while not solo_letras:
    sec = input('Ingresa una secuencia de letras: ')
    secuencia = sec.replace(" ", "").replace(",", "").replace(".", "").lower()
    if secuencia.isalpha():
        solo_letras = True


# Verifica que el orden de las letras es el mismo
# de izquierda a derecha que de derecha a izquierda.
longitud = len(secuencia)
palindromo = True
for letra1, letra2 in zip(secuencia[:longitud//2], secuencia[longitud-1:longitud//2 + 1:-1]):
    if letra1 != letra2:
        palindromo = False


# Se despliega el resultado
if palindromo:
    print('La secuencia', sec, 'es un palindromo')
else:
    print('La secuencia', sec, 'no es palindromo')
print()
