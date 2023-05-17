"""
Programa torre_blanca.py
Autor: Abel García

Indica si una torre blanca puede capturar a alguna de
las piezas negras en un tablero de ajedrez.

Considera que las columnas y las filas de un tablero
de ajedrez están numeradas del 1 al 8, tanto de
izquierda a derecha como de abajo hacia arriba. En
una partida, la torre blanca está en alguna casilla
(x,y), en donde x representa la posición horizontal y
y la vertical. Esta pieza se puede mover cualquier
cantidad de casillas a la izquierda o derecha sobre
la misma fila o hacia arriba o abajo sobre la misma
columna.

Este programa coloca de forma aleatoria un numero de
piezas negras dado por el usuario. Después, le pide la posición de la torre blanca dentro del tablero.



1. Constantes:
    Ninguna
    
2. Los datos de entrada son:
    n - la cantidad de piezas negras (<= 8).
    (x,y) - la posición de la torre blanca.

3. Cálculos:
    Dada la posición (x,y) de la torre blanca,
    verifica si hay piezas negras hacia:
    a) la izquierda.
    b) la derecha.
    c) arriba.
    d) abajo.

4. Los datos de salida son:
    Las posiciones en donde están las piezas negras
    que pueda cpaturar la torre blanca.
"""

from random import choice


"""
Se recibe el número de piezas negras para colocar
en el tablero.
"""
print()
num_piezas_ok = False
while not num_piezas_ok:
    n = input('Ingresa la cantidad de piezas negras (máximo 8): ')
    if n.isdigit() and int(n) <= 8:
        num_piezas_ok = True
n = int(n)


"""
Representamos un tablero como un arreglo
bidimensional, en donde un . significa que la casilla
está libre.
"""
tablero = []
i = 0
while i < 8:
    tablero.append([])
    j = 0
    while j < 8:
        tablero[i].append('.')
        j = j + 1
    i = i + 1


"""
Se colocan en el tablero las piezas negras en una
posición aleatoria. La pieza se representa con la
letra N.
"""
i = 0
while i < n:
    # La función choice elige un número entre 0 y 7
    # de forma aleatoria
    x = choice(range(8))
    y = choice(range(8))
    if tablero[x][y] == '.':
        tablero[x][y] = 'N'
        i = i + 1


"""
Muestra en pantalla el tablero con las piezas negras.
"""
for j in range(7, -1, -1):
    print(j+1, end=' ')
    for i in range(8):
        print(tablero[i][j], end =' ')
    print()
print(' ', end =' ')
for i in range(8):
    print(i+1, end =' ')
print('\n')


"""
Recibe la posición (x,y) de la torre blanca. Si la
posición es válida y no está ocupada la casilla,
coloca la torre blanca y la representa con la letra T.
"""
torre_ok = False
while not torre_ok:
    torre_x_ok = False
    # Verifica que la posición x sea correcta
    while not torre_x_ok:
        x = input('Columna de la torre blanca: ')
        if x.isdigit() and int(x) >= 1 and int(x) <= 8:
            torre_x_ok = True
            x = int(x)
        else:
            print('Valor incorrecto')
            
    # Verifica que la posición y sea correcta
    torre_y_ok = False
    while not torre_y_ok:
        y = input('Fila de la torre blanca: ')
        if y.isdigit() and int(y) >= 1 and int(y) <= 8:
            torre_y_ok = True
            y = int(y)
        else:
            print('Valor incorrecto')

    # Si la posición (x,y) es correcta, se coloca la
    # torre
    if torre_x_ok and torre_y_ok:
        if tablero[x-1][y-1] == '.':
            tablero[x-1][y-1] = 'T'
            torre_ok = True


"""
Muestra en pantalla el tablero con las piezas negras
y la torre blanca.
"""
print()
for j in range(7, -1, -1):
    print(j+1, end=' ')
    for i in range(8):
        print(tablero[i][j], end =' ')
    print()
print(' ', end =' ')
for i in range(8):
    print(i+1, end =' ')
print('\n')


"""
Busca piezas negras a la izquierda de la torre blanca.
Si existe una, la captura y la marca con la letra X.
"""
i = x - 1
while i > 0:
    if tablero[i-1][y-1] == 'N':
        print('La torre blanca puede capturar a la pieza en (' + str(i) + ',' + str(y) + ')')
        tablero[i-1][y-1] = 'X'
        i = 0
    i = i - 1


"""
Busca piezas negras a la derecha de la torre blanca.
Si existe una, la captura y la marca con la letra X.
"""
i = x + 1
while i <= 8:
    if tablero[i-1][y-1] == 'N':
        print('La torre blanca puede capturar a la pieza en (' + str(i) + ',' + str(y) + ')')
        tablero[i-1][y-1] = 'X'
        i = 9
    i = i + 1


"""
Busca piezas negras abajo de la torre blanca.
Si existe una, la captura y la marca con la letra X.
"""
j = y - 1
while j > 0:
    if tablero[x-1][j-1] == 'N':
        print('La torre blanca puede capturar a la pieza en (' + str(x) + ',' + str(j) + ')')
        tablero[x-1][j-1] = 'X'
        j = 0
    j = j - 1


"""
Busca piezas negras arriba de la torre blanca.
Si existe una, la captura y la marca con la letra X.
"""
j = y + 1
while j <= 8:
    if tablero[x-1][j-1] == 'N':
        print('La torre blanca puede capturar a la pieza en (' + str(x) + ',' + str(j) + ')')
        tablero[x-1][j-1] = 'X'
        j = 9
    j = j + 1


"""
Muestra en pantalla el tablero con las piezas negras, las capturadas, y la torre blanca.
"""
print()
for j in range(7, -1, -1):
    print(j+1, end=' ')
    for i in range(8):
        print(tablero[i][j], end =' ')
    print()
print(' ', end =' ')
for i in range(8):
    print(i+1, end =' ')
print('\n')

