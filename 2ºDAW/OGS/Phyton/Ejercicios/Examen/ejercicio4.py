#Suma de numeros
#Pide un numero N y calcula la suma de todos los números desde 1 hasta N usa bucle for con un rango adecuado
N = int(input("Introduce un número: "))

# Inicializar la variable suma
suma = 0

# Usar un bucle for para sumar los números del 1 al N
for i in range(1, N + 1):
    suma += i

# Mostrar el resultado
print(f"La suma de los números del 1 al {N} es: {suma}")

   