"""
Programa estacion.py
Autor: Abel García

Indica la estación a la que pertenece una fecha dada,
de acuerdo con:

    Estación        Fecha de inicio
    Primavera       20 de marzo
    Verano          21 de junio
    Otoño           22 de septiembre
    Invierno        21 de diciembre


1. Constantes:
    Ninguna.
    
2. Los datos de entrada son:
    día
    mes

3. Cálculos:
    a) Se debe verificar cuál es el mes. Si el mes
        completo corresponde a una estación,
        indicarlo.
        
    b) Si el mes corresponde a dos estaciones,
        verificar si el día es previo al inicio de
        la siguiente estación.

4. Los datos de salida son:
    La estación correspondiente a la fecha.
"""

# Se piden los datos de entrada
print()
dia = int(input("Introduce el dia: "))
mes = int(input("Introduce el mes: "))


# Cálculos para saber a qué estación corresponde
# la fecha

# enero o febrero es invierno
if mes == 1 or mes == 2:
    estacion = 'invierno'
    
# marzo corresponde a dos estaciones, depende
# del día
elif mes == 3:
    # antes del 20 es invierno
    if dia < 20:
        estacion = 'invierno'
    # del 20 en adelante es primavera
    else:
        estacion = 'primavera'

# abril y mayo es primavera
elif mes == 4 or mes == 5:
    estacion = 'primavera'

# junio corresponde a dos estaciones, depende
# del día
elif mes == 6:
    # antes del 21 es primavera
    if dia < 21:
        estacion = 'primavera'
    # del 21 en adelante es verano
    else:
        estacion = 'verano'

# julio y agosto es verano
elif mes == 7 or mes == 8:
    estacion = 'verano'

# septiemre corresponde a dos estaciones, depende
# del día
elif mes == 9:
    # antes del 22 es verano
    if dia < 22:
        estacion = 'verano'
    # del 22 en adelante es otoño
    else:
        estacion = 'otoño'

# octubre y noviembres es otoño
elif mes == 10 or mes == 11:
    estacion = 'otoño'
    
# diciembre corresponde a dos estaciones, depende
# del día
elif mes == 12:
    # antes del 21 es otoño
    if dia < 21:
        estacion = 'otoño'
    # del 21 en adelante es invierno
    else:
        estacion = 'invierno'


# Se despliega el resultado
print('Le fecha', dia, '/', mes, 'corresponde a', estacion)
print()
