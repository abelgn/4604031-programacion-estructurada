"""
Programa potencia.py
Autor: Abel García

Este programa calcula la potencia de x a la n.

1. Constantes:
    Ninguna

2. Los datos de entrada son:
    x, la base.
    n, la potencia.

3. Cálculos:
    La potencia se calcula multiplicando n veces x.

4. Los datos de salida son:
    La potencia de x a la n.
"""


def recibir_numero():
    """
    Pide el dato de entrada x.
    Se espera que el dato que se ingrese sea un número.
    Devuelve el número de entrada.
    """

    es_numero = False
    while not es_numero:
        x = input('Ingresa la base: ')
        if x.replace(".", "").replace("-","").isdigit():
            es_numero = True
        else:
            print('No válido.')
    return float(x)


def recibir_entero():
    """
    Pide el dato de entrada n.
    Se espera que el dato que se ingrese sea un número entero.
    Devuelve el número de entrada.
    """

    es_entero = False
    while not es_entero:
        n = input('Ingresa la potencia: ')
        if n.replace("-", "").isdigit():
            es_entero = True
        else:
            print('No válido.')
    return int(n)


def potencia(x, n):
    """ 
    Calcula y devuelve la potencia de x a la n. 
    """
    resultado = 1
    if n < 0:
        potencia = -1 * n
    else:
        potencia = n
    while potencia >= 1:
        resultado = resultado * x
        potencia = potencia - 1
    if n < 0:
        resultado = 1.0 / resultado
    return resultado


def main():
    print()
    x = recibir_numero()
    n = recibir_entero()
    pot = potencia(x, n)
    print(pot)
    print()


main()
