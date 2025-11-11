#Utilizando FOR dibuja por pantalla un triángulo rectángulo de
#* cuya altura sea dada por el usuario. Por ejemplo, si el usuario
#indica un tres el triángulo que debe pintar en pantalla sería así:

# Pedir al usuario la altura del triángulo
altura = int(input("Introduce la altura del triángulo: "))

# Usar un bucle for para dibujar el triángulo
for i in range(1, altura + 1):
    print("*" * i)  