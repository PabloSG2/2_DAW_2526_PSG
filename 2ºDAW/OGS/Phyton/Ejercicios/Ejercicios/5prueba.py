print("----FOR---")
cadena = input('Introduzca una palabra ')
for letra in cadena:
    print(letra)

print("\n----WHILE---")
contador = 1
while contador <= 100:
    print(contador)
    contador += 1
    
print("\n----RANGE---")
for i in range(1,11):
    print(f'\nTabla del {i}\n------------')
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}')
        