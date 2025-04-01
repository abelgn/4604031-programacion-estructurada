# Módulo de números primos

"""
Provee funciones para trabajar con números primos.

Al momento solo incluye cuatro funciones:
es_primo(x)
es_primo_mersenne(x)
siguiente_primo(x)
anterior_primo(x)
"""


def es_primo(x):
    """
    Verifica si un número x es primo.

    Un número x es primo si x > 1 y si sólo es divisible
    entre 1 y él mismo.

    Devuelve True si x es primo, False en caso contrario.
    """
    from math import sqrt

    primo = True
    if x <= 1:
        primo = False
    i = 2
    max_i = sqrt(x)
    while primo and i <= max_i:
        if x % i == 0:
            primo = False
        else:
            i = i + 1
    return primo


def es_primo_mersenne(x):
    """
    Verifica si un número x es primo de Mersenne.

    Un número x es primo de Mersenne si es primo y además
    2^x - 1 también es primo.

    Devuelve True si x es primo de Mersenne, False en caso contrario.
    """

    primo_mersenne = False
    primo = es_primo(x)
    if primo:
        y = 2 ** x - 1
        primo_mersenne = es_primo(y)
    return primo_mersenne


def siguiente_primo(x):
    """Devuelve el siguiente número primo mayor que x."""

    x = x + 1
    primo = False
    while not primo:
        if es_primo(x):
            primo = True
        else:
            x = x + 1
    return x


def anterior_primo(x):
    """Devuelve el anterior número primo menor que x."""

    x = x - 1
    primo = False
    while not primo and x > 1:
        if es_primo(x):
            primo = True
        else:
            x = x - 1
    return x


if __name__ == "__main__":
    import sys
    print(es_primo(int(sys.argv[1])))
