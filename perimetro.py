"""
Programa perimetro.py
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


from math import sqrt


# Recibe el número de lados del polígono
print()
num_lados = input("¿Cuántos lados tiene el polígono? ")
while (len(num_lados) == 0) and not num_lados.isdigit():
    print('Entrada no válida.')
    num_lados = input("¿Cuántos lados tiene el polígono? ")
num_lados = int(num_lados)


# Recibe las coordenadas de los vértices del polígono
vertices = []
i = 0
while i < num_lados:
    xi_ok = False
    # Verifica que la coordenada xi sea correcta
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
            
    vertices.append([float(xi), float(yi)])
    i = i + 1


# Calcula la distancia entre dos vértices y acumula
# la longitud
i = 0
perimetro = 0.0
while i < num_lados-1:
    difx = vertices[i][0] - vertices[i+1][0]
    dify = vertices[i][1] - vertices[i+1][1]
    perimetro = perimetro + sqrt(difx**2 + dify**2)
    i = i + 1
difx = vertices[i][0] - vertices[0][0]
dify = vertices[i][1] - vertices[0][1]
perimetro = perimetro + sqrt(difx**2 + dify**2)


# Se despliega el resultado
print('El perímetro del polígono es: ', perimetro)
print()
