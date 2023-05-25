"""
Programa: nomina.py
Autor: Abel García

En una empresa, para obtener el sueldo bruto mensual
de una persona se tienen las siguientes reglas:

* Cada persona tiene un salario por hora laborada.
* Si las horas de trabajo al mes son inferiores o
iguales a 160, simplemente se paga el salario por
hora trabajada.
* Si las horas exceden las 160 pero no pasan de 200,
las primeras 160 horas se pagan de acuerdo al salario
por hora y las excedentes se pagan como extra, donde
cada hora extra se paga a 1.5 el salario por hora.
* Si el empleado trabajó más de 200 horas, se aplica
el criterio anterior y las horas excedentes a 200 se
pagan como doble extra, donde cada hora doble extra
se paga al doble del salario por hora.

Cada persona tiene derecho a una comisión de acuerdo
con el porcentaje de cumplimiento de sus objetivos de
desempeño:

* Menor del 50%, no tiene derecho a comisión.
* Desde 50% y hasta 75%, tiene derecho al 2% de su
sueldo bruto.
* Desde 76 y hasta 90%, tiene derecho al 5% de su
sueldo bruto.
* Desde 91 y hasta 99%, tiene derecho al 10% de su
sueldo bruto.
* Con el 100%, tiene derecho al 20% de su sueldo
bruto.

Los impuestos a deducir a la persona se calculan
según el sueldo bruto mensual:

* Sueldos menores o iguales a $4,000 no pagan
impuestos.
* Hasta $20,000, pagan el 20% del excedente de
$4,000.00.
* Hasta $30,000, pagan el impuesto anterior más 25%
del excedente de $20,000.
* Los sueldos arriba de $30,000.00, pagan los
impuestos anteriores, más el 35% del excedente de
$30,000.

En cuanto a seguridad social, la aportación de cada
persona es del 2.5% de su sueldo bruto, sin importar
la cantidad de este.

Adicionalmente, si la persona está registrada en la
caja de ahorros de la empresa, se le descuenta su
ahorro de acuerdo con los siguientes tipos de
participaciones:

* Cuota fija, en donde su ahorro es de $1,000.00
mensuales.
* Cuota porcentual, en donde puede ahorrar mensualmente:
- El 3% de su sueldo mensual bruto o
- El 5% de su sueldo mensual bruto.

Por otro lado, respecto al fondo de ahorro para el
retiro, las personas tienen derecho al ahorro
solidario y tienen las siguientes tres opciones de
participación:

* No participar en el ahorro solidario.
* 1% del sueldo bruto mensual.
* 2% del sueldo bruto mensual.
"""

import entrada_teclado as et


def menu(titulo, opciones):
    """
    Despliega un menú con opciones.
    
    Devuelve la opción elegida por el usuario como un int.
    """
    
    opcion = len(opciones) + 1
    while opcion not in range(len(opciones) + 1):
        print(titulo)
        for i in range(len(opciones)):
            print(i + 1, opciones[i], sep=". ")
        print("0. Ninguna")
        opcion = et.recibir_entero_positivo("Opción: ")
        if opcion not in range(len(opciones) + 1):
            print("La opción no es válida")
    return opcion


def calcular_sueldo_bruto(horas, sueldo_hora):
    """Calcula el sueldo bruto mensual."""
    if horas <= 160:
        sueldo_bruto = horas * sueldo_hora
    elif horas <= 200:
        sueldo_bruto = (160 + 1.5 * (horas - 160)) * sueldo_hora
    else:
        sueldo_bruto = (160 + 1.5 * 40 + 2 * (horas - 200)) * sueldo_hora
    return sueldo_bruto


def calcular_comision(porcentaje_objetivos, sueldo_bruto):
    """Calcula la comisión."""
    if porcentaje_objetivos < 50:
        comision = 0.0
    elif porcentaje_objetivos <= 75:
        comision = sueldo_bruto * 0.02
    elif porcentaje_objetivos <= 90:
        comision = sueldo_bruto * 0.05
    elif porcentaje_objetivos < 100:
        comision = sueldo_bruto * 0.1
    else:
        comision = sueldo_bruto * 0.2
    return comision


def calcular_impuestos(sueldo_bruto):
    """Calcula la deducción por impuestos."""
    if sueldo_bruto <= 4000:
        impuestos = 0.0
    elif sueldo_bruto <= 20000:
        impuestos = (sueldo_bruto - 4000) * 0.2
    elif sueldo_bruto <= 30000:
        impuestos = 16000 * 0.2 + (sueldo_bruto - 20000) * 0.25
    else:
        impuestos = 16000 * 0.2 + 10000 * 0.25 + (sueldo_bruto - 30000) * 0.35
    return impuestos


def calcular_aportacion_caja(participacion_caja, sueldo_bruto):
    """Calcula la aportación a la caja de ahorro."""
    if participacion_caja == 0:
        caja = 0.0
    elif participacion_caja == 1:
        caja = 1000
    elif participacion_caja == 2:
        caja = sueldo_bruto * 0.03
    else:
        caja = sueldo_bruto * 0.05
    return caja


def calcular_aportacion_ahorro(participacion_ahorro, sueldo_bruto):
    """Calcula la aportación al ahorro solidario."""
    if participacion_ahorro == 0:
        ahorro = 0.0
    elif participacion_ahorro == 1:
        ahorro = sueldo_bruto * 0.01
    else:
        ahorro = sueldo_bruto * 0.02
    return ahorro


def main():
    # El salario por hora
    salario_hora = et.recibir_flotante_positivo("Salario por hora: ")

    # Las horas trabajadas en el mes
    horas = et.recibir_entero_positivo("Horas trabajadas en el mes: ")

    # El porcentaje de cumplimiento de los objetivos
    porcentaje_objetivos = et.recibir_flotante_positivo("Porcentaje de cumplimiento de los objetivos: ")

    # Participación en la caja de ahorros
    opciones = ["Cuota fija", "Cuota 3%", "Cuota 5%"]
    titulo = "Participación en la caja de ahorros"
    participacion_caja = menu(titulo, opciones)

    # Participación en el ahorro solidario
    opciones = ["1%", "2%"]
    titulo = "Participación en el ahorro solidario"
    participacion_ahorro = menu(titulo, opciones)

    # Cálculo de percepciones
    sueldo_bruto = calcular_sueldo_bruto(horas, salario_hora)
    comision = calcular_comision(porcentaje_objetivos, sueldo_bruto)
    
    # Total de percepciones
    percepciones = sueldo_bruto + comision
    
    # Cálculo de deducciones
    impuestos = calcular_impuestos(sueldo_bruto)
    caja = calcular_aportacion_caja(participacion_caja, sueldo_bruto)
    ahorro = calcular_aportacion_ahorro(participacion_ahorro, sueldo_bruto)

    # Total de deducciones
    deducciones = impuestos + caja + ahorro

    # Calculo del sueldo neto
    sueldo_neto = percepciones - deducciones

    print("*** Percepciones")
    print("Sueldo bruto mensual:\t\t\t%8.2f" % sueldo_bruto)
    print("Comision:\t\t\t\t%8.2f" % comision)
    print("Total de percepciones:\t\t\t%8.2f" % percepciones)
    print("*** Deducciones")
    print("Impuestos:\t\t\t\t%8.2f" % impuestos)
    print("Aportación a la caja de ahorros:\t%8.2f" % caja)
    print("Aportación al ahorro solidario:\t\t%8.2f" % ahorro)
    print("Total de deducciones:\t\t\t%8.2f" % deducciones)
    print("*** Sueldo neto a recibir:\t\t%8.2f" % sueldo_neto)


main()
