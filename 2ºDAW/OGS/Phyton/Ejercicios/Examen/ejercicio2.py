#Numero par o impar
num= int(input("Introduzca una numero: "))

#Hacemos un if comprobando que el numero se puede dividir entre 2 y de resto 0
if num % 2 == 0:
    print ("Numero par")
#Comprobamos que al no ser la primera condicion será impar
else:
    print ("Numero impar")