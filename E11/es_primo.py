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


def recibir_entero():
    """
    Pide el dato de entrada x.
    Se espera que el dato que se ingrese sea un número entero mayor que 1.
    Devuelve el número de entrada.
    """

    print()
    es_positivo = False
    while not es_positivo:
        x = input('Ingresa un número entero mayor que 1: ')
        if x.isdigit() and int(x) > 1:
            es_positivo = True
    return int(x)



def es_primo(x):
    """
    Verifica si x es un número primo.
    """
    k = 2
    primo = True
    while primo and k <= x/2:
        if x % k == 0:
            primo = False
        k = k + 1
    return primo


def main():
    x = recibir_entero()
    primo = es_primo(x)
    if primo:
        resp = 'es número primo'
    else:
        resp = 'no es número primo'
    print(x, resp)
    print()
    
    
main()
