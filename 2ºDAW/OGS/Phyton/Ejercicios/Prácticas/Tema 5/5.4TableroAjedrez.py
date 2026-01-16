#Dibujar un tablero ajedrez mediante bucles for anidados

#Hacemos un for de 8*8 ya que eso ocupa el tablero
for fila in range(8):
    for columna in range(8):
        if (fila + columna) % 2 == 0:
            print(" ", end="")  # Casilla blanca y espacio en misma linea
        else:
            print("#", end="")  # Casilla negra y espacio en misma linea
    print()