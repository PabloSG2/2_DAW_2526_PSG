#Mostramos una tupla
dias = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes','Sábado','Domingo')
print("Mostramos día: " +dias[0])

#Iterar valores
valores = (1,5,2,7)
for valor in valores:
    print("Valor:",valor)

#Probamos lista
lista = ["Manuel", "pepe", "manuel",25]
print("Valor 2: " +lista[1])
lista[1]= "Pepe"
print("Valor 2 editado: "+lista[1]) 

#Sublistas
print(lista[:2]) #Sublista que muestra el valor 0 y 1
posicion = lista.index("Pepe") #Busqueda de un valor "Pepe"
print(f"Posicion Pepe: {posicion}")
del lista[3] 
print(f"{lista}")

#Busquedas
for listas in enumerate(lista): #recorrer una lista enumerada
    print(listas)

#Matrices
fila1 = [1,2,3]
fila2 = [4,5,6]
fila3 = [7,8,9]
matriz = [fila1,fila2, fila3]
print("Matriz:",matriz,"\nMatriz 1:",matriz[1])#Matriz completa y valor 1

#Diccionarios
lenguajes = { 'C':1972, 'python':1991, 'Java':1996}
for clave, valor in lenguajes.items():
    print(f"Lenguaje {clave} -> {valor}")

#Cadenas y colecciones
frase = 'Hola mundo'
palabra= frase.split()
print(palabra)

#Conjuntos
a = {1, 2, 3, 4}
b = {5, 6, 3, 7}
print(a | b) #Es = a.union(b) muestra lo mismo
print(a-b) #Muestra los que estan en uno y no el otro

#Zip
paises = ['Francia', 'Alemania','España']
capitales = ['París', 'Berlín','Madrid']
for pais,capital in zip(paises,capitales):
    print(f'{pais} capital {capital}')