#Introducimos en consola: saludo('Pepe',idioma='es') 

#Prueba de nombre con valor por defecto
def saludo(nombre = 'Python', idioma = 'en'):
    if idioma == 'es':
        print(f'Hola {nombre}')
    else:
        print(f'Hello {nombre}')
saludo('Pepe',idioma='es') #Prueba del codigo 

#Prueba de suma de numeros 
def suma(num1, num2):
    resultado= num1+num2
    return resultado

#Prueba factorial
def factorial(N):
    if N == 1:
        resultado = 1
    else:
        resultado = N* N-1
    return resultado
