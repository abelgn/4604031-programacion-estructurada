"""
Define el registro vector y funciones para calcular operaciones con
vectores.
"""

from math import acos, degrees, sqrt


def crear_vector(x, y, z):
    """
    Crea y devuelve un vector en tres dimensiones.

    El vector está definido como un diccionario con claves 'x', 'y','z',
    respectivamente para las componentes x, y, z.
    """
    return {'x': x, 'y': y, 'z': z}


def sumar(v1, v2):
    """Suma los vectores v1, v2 y v3 y devuelve el vector resultante."""
    suma = {'x': v1['x'] + v2['x'], 'y': v1['y'] + v2['y'],
            'z': v1['z'] + v2['z']}
    return suma


def magnitud(v):
    """Calcula y devuelve la magnitud del vector v."""
    mag = sqrt(v['x'] ** 2 + v['y'] ** 2 + v['z'] ** 2)
    return mag


def producto_escalar(v1, v2):
    """Calcula y devuelve el producto escalar de los vectores
    v1 y v2."""
    prod = v1['x'] * v2['x'] + v1['y'] * v2['y'] + v1['z'] * v2['z']
    return prod


def producto_vectorial(v1, v2):
    """Calcula y devuelve el producto vectorial de los vectores
    v1 y v2."""
    x = v1['y'] * v2['z'] - v1['z'] * v2['y']
    y = v1['z'] * v2['x'] - v1['x'] * v2['z']
    z = v1['x'] * v2['y'] - v1['y'] * v2['x']
    return crear_vector(x, y, z)


def angulo(v1, v2):
    """Calcula y devuelve el ángulo que forman los dos vectores
    v1 y v2."""
    ang = degrees(acos(producto_escalar(v1, v2)
                       / (magnitud(v1) * magnitud(v2))))
    return ang
