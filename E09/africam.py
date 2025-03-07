"""
Programa africam.py
Autor: Abel García

Calcula el precio total de admisión para un grupo
de personas que desean visitar Africam Safari.

El precio de admisión en Africam Safari varía según
la edad del visitante. Los niños menores de 3 años
no pagan. Los niños de 3 a 11 años pagan $340. A
partir de 12 años pagan $350. Presentando su tarjeta
del INAPAM, los adultos mayores (60 años o más)
tienen 50% de descuento.


1. Constantes:
    precio:_menor = 385
    precio_adulto = 375
    edad_menor = 3
    edad_adulto = 12
    edad_inapam = 60
    precio_inapam = 192
    
2. Los datos de entrada son:
    edades de los visitantes

3. Cálculos:
    Por cada edad de entrada:
        a) Incrementar el total de acuerdo con el precio.
        b) Cuando aplique, considerar el descuento.

4. Los datos de salida son:
    El precio de admisión para todo el grupo.
"""


# Inicialización de constantes
precio_menor = 375
precio_adulto = 385
edad_menor = 3
edad_adulto = 12
edad_inapam = 60
precio_inapam = 192

mensaje = 'Ingresa la edad del visitante o solo enter para continuar: '

# Inicialización del precio total de admisión
precio_total = 0.0

# Se piden los datos de entrada
print()
texto = input(mensaje)

# El ciclo continúa mientras haya una edad como entrada
while len(texto) > 0:
    if texto.isdigit():
        edad = int(texto)

        # Se clasifica la edad de la persona de acuerdo con
        # los rangos de precios
        if edad < edad_menor:
            precio = 0
        elif edad < edad_adulto:
            precio = precio_menor
        elif edad < edad_inapam:
            precio = precio_adulto
        else:
            inapam = input ('Presenta tarjeta INAPAM [s/n]: ')
            if inapam.lower() == 's':
                precio = precio_inapam
            else:
                precio = precio_adulto


        # Se muestra el precio individual
        print('Precio: $%6.2f' % precio)

        # Se incrementa el precio total de admisión
        precio_total = precio_total + precio

    else:
        print('Entrada no válida.')

    texto = input(mensaje)


# Se despliega el resultado
print('El precio total de admisión es $%7.2f' % precio_total)
print()

