"""
Programa: directorio_telefonico.py
Autor: Abel García

Simula un directorio telefónico.

Solicita al usuario el nombre, apellido y número de teléfono
de cada persona que ingresará al directorio.
"""


def recibir_datos():
    """Pide al usuario el nombre, apellido y número de teléfono de
    una persona y devuelve estos datos."""
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    numero = int(input('Número:'))
    return nombre, apellido, numero


def crear_registro(nombre, apellido, numero):
    """Crea un registro con el nombre, apellido y número de teléfono
    de una persona."""
    registro = {'nombre': nombre, 'apellido': apellido,
                'numero': numero}
    return registro


def mostrar_directorio(directorio):
    """Muestra en pantalla el contenido del directorio."""
    for registro in directorio:
        print(registro['nombre'] + '\t\t' + registro['apellido'] \
        + '\t\t' + str(registro['numero']))


def main():
    directorio = []
    respuesta = 's'
    while respuesta.upper() == 'S':
        respuesta = input('\n¿Nuevo registro? [S/N] ')
        if respuesta.upper() == 'S':
            nombre, apellido, numero = recibir_datos()
            registro = crear_registro(nombre, apellido, numero)
            directorio.append(registro)
    mostrar_directorio(directorio)


main()
