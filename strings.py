"""
Programa strings.py
Autor: Abel García

Este programa muestra ejemplos sobre el uso de strings
y algunas operaciones.
"""

# Los strings son secuencias de caractares
# entre comillas dobles
print("Hola")

# o comillas secillas (opción preferida)
print('Hola')

# La cadena vacía es una cadena sin caracteres
print("")

print('')

# Algunas secuencias de escape
# \b  Retroceso
# \n  Salto de línea
# \t  Tabulador
# \\  Diagonal invertida
# \'  Comilla simple
# \"  Comilla doble
print('Hola\bamigos')

print('Hola\namigos')

print('Hola\tamigos')

print('Hola\\amigos')

print('Hola\'amigos')

print('Hola\"amigos')


# Cada carácter del conjunto ASCII tiene su
# correspondiente valor entero.
# La función chr convierte un carácter a entero
ord('a')

# La función ord hace lo inverso.
chr (65)

chr( ord('A') + 3)


# La longitud de una cadena es el número de caracteres
# que contiene.
# La función len de Python devuelve la longitud.
len('Buenos dias')

len('')

# Las posiciones de los caracteres en un string están
# numeradas, de izquierda a derecha, desde 0 hasta la
# longitud de la cadena menos uno.
# El operador de subíndice [] permite inspeccionar el
# carácter en una posición determinada en un string.
nombre = 'Alan Turing'

nombre[0]

nombre[3]

nombre[6]

nombre[len(nombre)]

nombre[len(nombre) - 1]

nombre[-1]



# El operador de subíndice también se puede usar para
# obtener una subcadena.
# Para extraer una subcadena, se colocan dos puntos (:)
# en el subíndice.
# Un valor entero puede aparecer en cualquier lado de los
# dos puntos.
nombre = 'miscript.py'

nombre[0:]

nombre[0:1]

nombre[0:2]

nombre[:5]

nombre[:len(nombre)]

nombre[-2:]

nombre[-8:-2]




# El operador in busca una subcadena en una cadena.
# Cuando se utiliza con cadenas, el operando izquierdo
# del operador in es una subcadena a buscar y el operando
# derecho es la cadena destino.
# El operador in devuelve True si la subcadena a buscar
# está en algún lugar de la cadena destino o False en
# caso contrario.
nombre = 'Alan Turing'

'A' in nombre

'an Tu' in nombre

'Hola' in nombre


# La función print comienza automáticamente a escribir un
# dato de salida en la primera columna disponible.
# Python incluye un mecanismo de formato general que
# permite especiicar anchos de campo para diferentes
# tipos de dato.
'%6s' % 'cinco'

'%-6s' % 'cinco'

exponente = 9

print ('%-3d%12d' % (exponente, 10 ** exponente))

exponente = 10

print ('%-3d%12d' % (exponente, 10 ** exponente))


salario = 100

print ('Tu salario es $' + str(salario))

print ('Tu salario es $%0.2f' % salario)

print ('Tu salario es $%6d' % salario)

print ('Tu salario es $%8.2f' % salario)

print ('Tu salario es $%08.2f' % salario)
