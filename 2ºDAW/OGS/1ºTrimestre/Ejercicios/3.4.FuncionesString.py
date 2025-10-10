#Elabora un programa donde se utilice las funciones String
#estudiadas en los apuntes del tema: len, replace, strip, lower,
#upper, capitalize, title y swapcase. Utiliza comentarios explicativos

# Se Introduce una palabra o frase
palabra = input('Introduzca una palabra o frase: ')

# Mostrar la longitud de la palabra o frase
print('La palabra "'+palabra+'" mide '+str(len(palabra))+' caracteres.')

# Reemplazar todas las letras 'a' por 'e' en la cadena
nueva_palabra = palabra.replace('a', 'e')
print(palabra, '->', nueva_palabra)

# Eliminar posibles saltos de línea al inicio o final 
strip_palabra = palabra.strip('\n')
print(palabra, '->', strip_palabra)

# Convertir toda la cadena a minúsculas
print('Minúsculas:', palabra.lower())

# Convertir toda la cadena a mayúsculas
print('Mayúsculas:', palabra.upper())

# Capitalizar la primera letra de toda la cadena
print('Capitalizada:', palabra.capitalize())

# Convertir la primera letra de cada palabra a mayúscula
print('Título:', palabra.title())

# Cambiar mayúsculas a minúsculas y viceversa
print('Swapcase:', palabra.swapcase())