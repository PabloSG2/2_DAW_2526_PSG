import math
import random

class AnimacionesPaso:
    def __init__(self, tipo):
        self.tipo = tipo
        self.t = 0

        self.vibracion_val = 0
        self.mecia_val = 0
        self.cintura_val = 0
        self.costero_val = 0

        self.act_picaito = False
        self.act_mecia = False
        self.act_cintura = False
        self.act_costero = False

    def actualizar(self):
        self.t += 0.15

        # PICÁITO
        self.vibracion_val = random.randint(-6, 6) if self.act_picaito else 0

        # MECÍA
        if self.act_mecia:
            if self.tipo == "cristo":
                self.mecia_val = math.sin(self.t * 1.2) * 4
            else:
                self.mecia_val = math.sin(self.t * 0.8) * 8
        else:
            self.mecia_val = 0

        # CINTURA (solo palio)
        self.cintura_val = math.sin(self.t * 0.6) * 12 if self.act_cintura and self.tipo == "palio" else 0

        # COSTERO (solo cristo)
        self.costero_val = math.sin(self.t * 1.5) * 10 if self.act_costero and self.tipo == "cristo" else 0

    def set_picaito(self, e): self.act_picaito = e
    def set_mecia(self, e): self.act_mecia = e
    def set_cintura(self, e): self.act_cintura = e
    def set_costero(self, e): self.act_costero = e
