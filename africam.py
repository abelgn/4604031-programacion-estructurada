"""
Programa es_primo.py
Autor: Abel García

El precio de admisión en Africam Safari varía según la edad del visitante. Los niños menores de 3 años no pagan. Los niños de 3 a 11 años pagan $340. A partir de 12 años pagan $350. Presentando su tarjeta del INAPAM, los adultos mayores (60 años o más) tienen 50% de descuento.

Escribe un programa que reciba del usuario las edades de un grupo de personas, con una edad en cada línea. El usuario ingresará una línea en blanco para indicar que no hay más invitados en el grupo. El programa debe mostrar el precio de admisión para el grupo con un mensaje apropiado.


1. Constantes:
    precio:_menor = 340
    precio_adulto = 350
    edad_menor = 3
    edad_adulto = 12
    edad_inapam = 60
    descto_inapam = 0.5
    
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
precio_menor = 340
precio_adulto = 350
edad_menor = 3
edad_adulto = 12
edad_inapam = 60
descto_inapam = 0.5

mensaje = 'Ingresa edad del visitante o solo enter para continuar: '


# Se piden los datos de entrada
texto = input(mensaje)




precio_total = 0.0

# El ciclo continua mientras haya una edad como entrada
while len(texto) > 0:
    edad = int(texto)
    
    # Se clasifica la edad de la persona de acuerdo con
    # los rangos de precios
    if edad < edad_menor:
        precio = 0
    elif edad < edad_adulto:
        precio = precio_menor
    else:
        precio = precio_adulto
        if edad >= edad_inapam:
            inapam = input ('Presenta tarjeta INAPAM [s/n]: ')
            if inapam.lower() == 's':
                precio = precio * descto_inapam
    
    # Se muestra el precio individual
    print('Precio: $%6.2f' % precio)
    
    # Se incrementa el precio de admisión
    precio_total = precio_total + precio
    texto = input(mensaje)


# Se despliega el resultado
print ('El precio total de admisión es $%7.2f' % precio_total)
print()

