"""
Programa listas.py
Autor: Abel García

Este programa muestra ejemplos sobre el uso de listas
y algunas operaciones.
"""

# Las listas son secuencias de datos
# separados por comas
[1940 , 1975 , 2011]

['manzanas', 'naranjas', 'cerezas']

[]


# Se pueden usar otras listas como elementos de una lista.
[[5, 9], [541, 78]]


# Cuando el intérprete de Python evalúa una lista,
# también evalúa las expresiones en sus elementos.
import math

x = 9.876

[math.sqrt(2), math.pi, x]


# La función range genera una secuencia de enteros y
# con la función list podemos obtenerlos como una lista.
lista1 = [1, 2, 3, 4]

lista2 = range(1 ,5)

lista1

lista2

list(lista2)


# La función len devuelve la longitud de una lista.
lista1 = [1, 2, 3, 4]

lista2 = range(1 ,5)

len(lista1)

len(lista2)


# El operador de subíndice [] trabaja como en los strings.
lista1 = [1, 2, 3, 4]

lista2 = range(1 ,5)

lista1[0]

lista1[2:4]


# El operador + se usa sobre listas para su concatenación.
lista1 = [1, 2, 3, 4]

lista2 = range(1 ,5)

lista1 + [5 , 6]

lista1 + list(lista2)


# El operador de igualdad == compara dos listas.
lista1 = [1, 2, 3, 4]

lista2 = range(1 ,5)

lista1 == [4 , 5]

lista1 == list(lista2)


# Podemos usar el operador in para detectar la presencia
# o ausencia de un elemento en una lista.
lista1 = [1, 2, 3, 4]

lista2 = range(1 ,5)

3 in lista1

[3 , 4] in lista1

0 in lista1

2 in lista2


# Una lista se puede modificar, es decir, es mutable.
# En cualquier momento de su vida útil, los elementos
# se pueden insertar, eliminar o reemplazar.
lista = [1, 2, 3, 4]

lista

lista[3]

lista[3] = 99

lista


# La propiedad de mutabilidad de las listas conduce a
# algunos fenómenos interesantes.
primero = [10, 20, 30]

segundo = primero

primero

segundo

primero[1] = 99

primero

segundo


# El operador is de Python se puede usar para probar
# la identidad del objeto. Devuelve verdadero si los
# dos operandos se refieren exactamente al mismo objeto
# y devuelve falso si los operandos se refieren a objetos
# distintos (incluso si son estructuralmente equivalentes).
primero = [10, 20, 30]

segundo = primero

tercero = [10, 20, 30]

primero == segundo

primero == tercero

primero is segundo

primero is tercero
