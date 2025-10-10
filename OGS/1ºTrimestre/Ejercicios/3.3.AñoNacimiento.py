#Crea un programa que pida la edad por pantalla y calcule el año de nacimiento.
#NOTA: no tendremos en cuenta la fecha exacta.

nombreUsuario = input("¿Como te llamas? ")
edad = int(input("¿Dime tu edad? "))
fechaNacimiento= 2025 - edad
print("Hola",nombreUsuario, "naciste en:" ,fechaNacimiento)