"""
Define algunas funciones que simulan comandos de UNIX.
"""

from os.path import isfile


def head(nombre_archivo):
    """
    Muestra las primeras 10 líneas del archivo cuyo nombre se
    proporciona como parámetro.
    
    Devuelve True si el archivo existe, False en caso contrario.
    """
    existe = True
    if isfile(nombre_archivo):
        NUM_LINEAS = 10
        num_linea = 0
        f = open(nombre_archivo, 'r')
        linea = f.readline()
        while linea != '' and num_linea < NUM_LINEAS:
            num_linea = num_linea + 1
            print(linea.strip())
            linea = f.readline()
        f.close()
    else:
        existe = False
    return existe


def tail(nombre_archivo):
    """
    Muestra las últimas 10 líneas del archivo cuyo nombre se proporciona
    como parámetro.
    
    Devuelve True si el archivo existe, False en caso contrario.
    """
    existe = True
    if isfile(nombre_archivo):
        NUM_LINEAS = 10
        num_linea = 0
        f = open(nombre_archivo, 'r')
        lineas = []
        linea = f.readline()
        while linea != '':
            lineas.append(linea.strip())
            num_linea += 1
            if num_linea > NUM_LINEAS:
                lineas.pop(0)
                num_linea -= 1
            linea = f.readline()
        f.close()
        for linea in lineas:
            print(linea)
    else:
        existe = False
    return existe


def cat(nombres_archivos):
    """
    Concatena y muestra el contenido de los archivos cuyos nombres
    se proporcionan como parámetro en una lista.
    
    Devuelve True si todos los archivos existen, False en caso
    contrario.
    """
    existe = True
    for nom_arch in nombres_archivos:
        if isfile(nom_arch):
            f = open(nom_arch, 'r')
            print(f.read())
            f.close()
        else:
            existe = False
    return existe
