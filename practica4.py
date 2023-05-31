"""
Programa: practica4.py
Autora:

Lee el texto de un archivo y usa el módulo legibilidad
para calcular el índice de Fernandez Huerta y para
decidir el nivel de legibilidad del texto.
"""

import legibilidad


def leer_texto():
    """Lee el contenido de un archivo de texto y lo devuelve."""
    nombre_archivo = input("Nombre del archivo de texto a analizar: ")
    archivo = open(nombre_archivo, 'r')
    texto = archivo.read()
    archivo.close()
    return texto


def mostrar_resultados(indice, nivel, oraciones, palabras, silabas):
    """Muestra en pantalla el resultado del análisis de un texto, de acuerdo
    con el índice de Fernández Huerta."""
    print('El índice de Fernández Huerta es %5.2f' % indice)
    print('El nivel de legibilidad es', nivel)
    print(oraciones, 'oraciones')
    print(palabras, 'palabras')
    print(silabas, 'sílabas')


def main():
    texto = leer_texto()
    oraciones, palabras, silabas, indice = legibilidad.indice_FH(texto)
    nivel = legibilidad.nivel_legibilidad_FH(indice)
    mostrar_resultados(indice, nivel, oraciones, palabras, silabas)


main()
