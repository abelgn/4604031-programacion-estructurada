"""
Programa password.py
Autor: Abel García

Algunos sistemas informáticos tienen ciertas
reglas para establecer contraseñas seguras,
de tal forma que estas deben cumplir con los
siguientes criterios:

1. Tener una longitud mínima de 8 caracteres.
2. Contener al menos un dígito.
3. Contener al menos una letra minúscula.
4. Contener al menos una letra mayúscula.
5. Contener al menos uno de los caracteres
!, #, $, %, &, /, (, ), =, ¿, ?, ¡, !, <, >,
*, +, -, _, [, ], {, }, @, |.

Este programa verifica si una secuencia de
caracteres forman una contraseña segura.

1. Constantes:
    especiales, una lista en donde se
    guardarán los caracteres especiales.

    long_minima, la longitud mínima de una
    contraseña segura
    
2. Los datos de entrada son:
    password, la secuencia de caracteres.

3. Cálculos:
    Verificar que la contraseña cumple con los
    cinco criterios arriba mencionados. Esto
    se logra recorriendo la contraseña,
    carácter por carácter.

    Si un carácter cumple con uno de los
    criterios, se registra.

    Al finalizar la verificación, todos los
    criterios deben estar registrados para
    decidir que la contraseña es segura.

4. Los datos de salida son:
    Verdadero en caso de que la contraseña
    sea segura, falso en caso contrario.
"""

# Se guardan los caracteres especiales en
# una lista
especiales = ['!', '#', '$', '%', '&', '/', \
              '(', ')', '=', '¿', '?', '¡', \
              '!', '<', '>', '*', '+', '-', \
              '_', '[', ']', '{', '}', '@', \
              '|']

# Longitud mínima de una contraseña segura
long_minima = 8

# Se pide la secuencia de caracteres.
print()
password = input('Ingresa la contraseña: ')
n = len(password)

# Inicialización de la variable para cada
# criterio
longitud = n >= long_minima
digito = False
minuscula = False
mayuscula = False
especial = False

# Variable que indica si la contraseña es
# segura
segura = False

# Si la contraseña cumple con la longitud
# mínima se verifican los demás criterios
if longitud:
    for i in password:
        if i.isdigit():
            digito = True
        elif i.islower():
            minuscula = True
        elif i.isupper():
            mayuscula = True
        elif i in especiales:
            especial = True

    segura = digito and minuscula \
             and mayuscula and especial

# Se despliega el resultado
if segura:
    print('La contraseña', password, \
          'es segura')
else:
    print('La contraseña', password, \
          'NO es segura')
print()
