"""
Programa perimetro_poligono.py
Autor: Abel García

Calcula el perímetro de un polígono, del cual se reciben las coordenadas de sus vértices.


1. Constantes:
    Ninguna.
    
2. Los datos de entrada son:
    Las coordenadas (xi, yi) de los vértices del
    polígono.

3. Cálculos:
    a) Se calcula la longitud del lado del polígono
        entre los vértices (xi,yi) y (xi+1, yi+1).
        
    b) Se suman todas las longitudes del polígono.

4. Los datos de salida son:
    El perímetro del polígono.
"""


def potencia(x, n):
    """
    Calcula la potencia de x elevada a la n.
    """
    resultado = 1.0
    if n < 0:
        exponente = -1 * n
    else:
        exponente = n
    while exponente >= 1:
        resultado = resultado * x
        exponente = exponente - 1
    if n < 0:
        resultado = 1.0 / resultado
    return resultado


def raiz_cuadrada(n):
    """
    Aproxima la raíz cuadrada de n.
    """
    aprox = n
    raiz = 1.0
    error = potencia(10, -10)
    while aprox - raiz > error:
        aprox = (aprox + raiz) / 2
        raiz = n / aprox
    return aprox


def numero_lados():
    """
    Recibe el número de lados del polígono.
    """
    print()
    n = input("¿Cuántos lados tiene el polígono? ")
    while (len(n) == 0) and not n.isdigit() and not int(n) >= 3:
        print('Entrada no válida.')
        n = input("¿Cuántos lados tiene el polígono? ")
    return int(n)


def recibir_vertice(i):
    """
    Recibe una coordenada del usuario y verifica que sea válida.
    """
    # Verifica que la coordenada xi sea correcta
    xi_ok = False
    while not xi_ok:
        xi = input('Coordenada x del vértice ' + str(i+1) + ': ')
        if xi.replace(".", "").isnumeric():
            xi_ok = True
        else:
            print('Valor incorrecto')

    # Verifica que la coordenada yi sea correcta
    yi_ok = False
    while not yi_ok:
        yi = input('Coordenada y del vértice ' + str(i+1) + ': ')
        if yi.replace(".", "").isnumeric():
            yi_ok = True
        else:
            print('Valor incorrecto')

    return float(xi), float(yi)


def recibir_vertices(num_lados):
    """
    Recibe las coordenadas de los vértices del polígono.
    """
    vertices = []
    for i in range(num_lados):
        xi, yi = recibir_vertice(i)
        vertices.append([xi, yi])
    return vertices


def calcular_distancia(x1, y1, x2, y2):
    """
    Calcula la distancia entre el par de vértices
    (x1,y1) y (x2,y2).
    """
    difx = x1 - x2
    dify = y1 - y2
    distancia = raiz_cuadrada(potencia(difx, 2) + potencia(dify, 2))
    return distancia


def calcular_perimetro(vertices):
    """
    Calcula el perímetro de un polígono dados sus vértices.
    """
    n = len(vertices)
    perimetro = calcular_distancia(vertices[n-1][0], vertices[n-1][1], \
                                   vertices[0][0], vertices[0][1])
    for i in range(n-1):
        perimetro = perimetro + calcular_distancia(vertices[i][0], vertices[i][1], \
                                                   vertices[i+1][0], vertices[i+1][1])
    return perimetro


def main():
    n = numero_lados()
    vertices = recibir_vertices(n)
    perimetro = calcular_perimetro(vertices)
    print('El perímetro del polígono es: ', perimetro)
    print()


main()
