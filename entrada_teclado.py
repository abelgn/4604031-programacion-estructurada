"""
Contiene funciones que reciben datos del teclado.
"""


def recibir_entero(mensaje):
    """
    Pide un número entero como dato de entrada.

    Devuelve el número entero de entrada como un int.
    """

    numero_ok = False
    while not numero_ok:
        n = input(mensaje)
        if n.replace("-", "", 1).isdigit():
            numero_ok = True
        else:
            print('Entrada no válida.')
    return int(n)


def recibir_entero_positivo(mensaje):
    """
    Pide un número entero positivo como dato de entrada.

    Devuelve el número entero positivo de entrada como un int.
    """

    numero_ok = False
    while not numero_ok:
        n = input(mensaje)
        if n.isdigit():
            numero_ok = True
        else:
            print('Entrada no válida.')
    return int(n)


def recibir_flotante(mensaje):
    """
    Pide un número de punto flotante como dato de entrada.

    Devuelve el número de punto flotante de entrada como un float.
    """

    numero_ok = False
    while not numero_ok:
        n = input(mensaje)
        if n.replace("-", "", 1).replace(".", "", 1).isdigit():
            numero_ok = True
        else:
            print('Entrada no válida.')
    return float(n)


def recibir_flotante_positivo(mensaje):
    """
    Pide un número de punto flotante positivo como dato de entrada.

    Devuelve el número de punto flotante positivo de entrada como
    un float.
    """

    numero_ok = False
    while not numero_ok:
        n = input(mensaje)
        if n.replace(".", "", 1).isdigit():
            numero_ok = True
        else:
            print('Entrada no válida.')
    return float(n)
