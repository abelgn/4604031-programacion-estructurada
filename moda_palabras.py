"""
Programa moda_palabras.py
Autor: Abel García

La moda de una lista de valores es el valor que ocurre con mayor
frecuencia. Este programa lee un archivo de texto, extra las
palabras en una lista e imprime su moda.

1. Constantes:
    Ninguna.
    
2. Los datos de entrada son:
    El nombre del archivo de texto a analizar.

3. Cálculos:
    El script utiliza una lista y un diccionario.

    La lista se utiliza para registrar las palabras del archivo de
    texto. El diccionario asocia cada palabra única con el número de
    ocurrencias en la lista.

    El script también usa la función max para calcular el máximo de
    dos valores. Cuando se usa con un solo argumento de lista, max
    devuelve el valor más grande que contiene.

4. Los datos de salida son:
    La palabra de moda y su frecuencia.
"""


def extraer_palabras(nombre_archivo):
    """
    Lee nombre_archivo para extraer las palabras que contiene el
    texto.

     Devuelve en una lista con las palabras del texto.
     """
    archivo = open(nombre_archivo, 'r')

    # Lee el texto línea por línea, convierte las palabras en
    # mayúsculas y agrega las palabras a una lista que será devuelta
    palabras = []
    for linea in archivo:
        palabras_linea = linea.split()
        for palabra in palabras_linea:
            palabras.append(palabra.upper())

    archivo.close()
    return palabras


def frecuencia_palabras(palabras):
    """
    Obtiene el conjunto de palabras únicas y sus frecuencias,
    guardando esta asociación en un diccionario.
    
    Devuelve un diccionario con las palabras y su frecuencia.
    """
    diccionario = {}
    for palabra in palabras:
        numero = diccionario.get(palabra, None)
        if numero is None:
            # palabra se ingresa por primera vez al diccionario
            diccionario[palabra] = 1
        else:
            # palabra ya ingresada, se incrementa su frecuencia
            diccionario[palabra] = numero + 1
    return diccionario
        
        
def encontrar_moda(diccionario):
    """
    Se encuentra la moda mediante el valor de la máxima frecuencia en
    el diccionario y se determina su clave.
    
    Devuelve la palabra de moda y su frecuencia.
    """
    maxima_frecuencia = max(diccionario.values())
    moda = []
    for clave in diccionario:
        if diccionario[clave] == maxima_frecuencia:
            moda.append(clave)
    return moda, maxima_frecuencia


def main():
    nombre_archivo = input('Nombre del archivo: ')
    palabras = extraer_palabras(nombre_archivo)
    diccionario = frecuencia_palabras(palabras)
    moda, frecuencia = encontrar_moda(diccionario)
    print('La moda es:', ','.join(moda), '\nFrecuencia:', str(frecuencia))


main()
