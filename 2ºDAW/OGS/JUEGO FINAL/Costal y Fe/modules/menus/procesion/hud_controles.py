import pygame
from core.botones import BotonSimple

class HUDControles:
    def __init__(self, tipo):
        self.tipo = tipo

        # Botones alineados en una sola fila
        self.botones = {
            "pausa": BotonSimple((20, 520, 150, 50), "Pausa"),
            "mas": BotonSimple((350, 520, 150, 50), "Más mecía"),
            "menos": BotonSimple((510, 520, 150, 50), "Menos mecía"),
        }

        if tipo == "cristo":
            self.botones["picaito"] = BotonSimple((180, 520, 150, 50), "Picaito")
            self.botones["costero"] = BotonSimple((670, 520, 150, 50), "Costero")

        else:  # Palio
            self.botones["cintura"] = BotonSimple((180, 520, 150, 50), "Cintura")

    def dibujar(self, ventana):
        for b in self.botones.values():
            b.dibujar(ventana)

    def click(self, pos):
        for nombre, boton in self.botones.items():
            if boton.clicado(pos):
                return nombre
        return None
