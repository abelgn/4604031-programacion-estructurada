"""
Programa es_par.py
Autor: Abel García

Este programa verifica si un número es par.

1. Constantes:
    Ninguna

2. Los datos de entrada son:
    n, el número a verificar si es par.

3. Cálculos:
    Un número es par si es divisible entre 2. Por lo tanto,
    se obtendrá el módulo 2 del número y se verificará si
    este es cero.

4. Los datos de salida son:
    Verdadero en caso de que el número sea par, falso en
    caso contrario.
"""


def recibir_entero():
    """
    Pide el dato de entrada n.
    Se espera que el dato que se ingrese sea un número entero.
    Devuelve el número de entrada.
    """

    entero = False
    while not entero:
        n = input('Ingresa un número entero: ')
        if n.replace("-", "").isdigit():
            entero = True
        else:
            print('No válido.')
    return int(n)


def es_par(n):
    """Verifica si n es par."""
    if n % 2 == 0:
        par = True
    else:
        par = False
    return par


def main():
    print()
    n = recibir_entero()
    if es_par(n):
        print(n, 'es par')
    else:
        print(n, 'es impar')
    print()
    

main()
