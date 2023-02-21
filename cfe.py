"""
Programa cfe.py
Autor: Abel García

Calcula el costo de consumo de energía eléctrica
de acuerdo con las tarifas de la CFE en la CDMX:

    Consumo básico, hasta 150 KWh, a $0.939 por unidad.
    Consumo intermedio, mayor a 150 y hasta 280 KWh, a $1.146 por unidad.
    Consumo excedente, mayor a 280 y hasta 500 KWh, a $3.346 por unidad.
    Tarifa Doméstica de Alto Consumo (DAC), mayor a 500 KWh, a $6.569 por unidad.


1. Constantes:
    t_basico = 0.939
    t_intermedio = 1.146
    t_excedente = 3.346
    t_dac = 6.569
    max_basico = 150
    max_intermedio = 280
    max_excedente = 500
    
2. Los datos de entrada son:
    consumo

3. Cálculos:
    De acuerdo con el consumo:
    a) Si está dentro del rango del consumo básico
        
        total = consumo * t_basico
        
    b) Si está dentro del rango del consumo intermedio
        
        total = max_basico * t_basico
                + (consumo - max_basico) * t_intermedio

    c) Si está dentro del rango del consumo excedente
        
        total = max_basico * t_basico
                + (max_intermedio - max_basico) * t_intermedio
                + (consumo - max_intermedio) * t_excedente
    
    d) Si el consumo corresponde a DAC
    
        total = consumo * t_dac

4. Los datos de salida son:
    total
"""


# Inicialización de las constantes
t_basico = 0.939
t_intermedio = 1.146
t_excedente = 3.346
t_dac = 6.569
max_basico = 150
max_intermedio = 280
max_excedente = 500



# Se piden los datos de entrada
print()
consumo = float(input("Introduce el consumo en KWh: "))


# Cálculos para conocer el costo del consumo

# Si el consumo es básico
if consumo <= max_basico:
    total = consumo * t_basico
elif consumo <= max_intermedio:
    total = max_basico * t_basico \
            + (consumo - max_basico) * t_intermedio
elif consumo <= max_excedente:
    total = max_basico * t_basico \
            + (max_intermedio - max_basico) * t_intermedio \
            + (consumo - max_intermedio) * t_excedente
else:
            total = consumo * t_dac


# Se despliega el resultado
print('El total a pagar por el consumo de', consumo, 'KWh es', total)
print()
