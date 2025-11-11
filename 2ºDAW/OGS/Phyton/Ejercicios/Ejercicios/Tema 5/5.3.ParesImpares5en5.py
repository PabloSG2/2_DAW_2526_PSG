#Con bucle for, ¿qué números de 1 a 100 y son par o impar?
#El recorrido será de 5 en 5, es decir, (1,6,11,...)

for numero in range(1, 101, 5): 
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")   
     