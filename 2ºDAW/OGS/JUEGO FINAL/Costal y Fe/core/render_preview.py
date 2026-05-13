import pygame

from modules.sprites.titular_sentencia import TitularSentencia
from modules.sprites.titular_macarena import TitularMacarena
from modules.sprites.paso_sentencia import PasoSentencia
from modules.sprites.paso_macarena import PasoMacarena
from modules.sprites.mod_banda import Banda
from modules.sprites.mod_habito import HabitoNazareno


def render_preview(tipo, estado=None):

    if tipo == "titular_cristo":
        surf = pygame.Surface((300, 350), pygame.SRCALPHA)
        TitularSentencia().dibujar(surf, 20, 10)
        return surf

    if tipo == "titular_virgen":
        surf = pygame.Surface((300, 350), pygame.SRCALPHA)
        TitularMacarena().dibujar(surf, 20, 10)
        return surf

    if tipo == "paso_cristo":
        surf = pygame.Surface((360, 260), pygame.SRCALPHA)
        PasoSentencia().dibujar(surf, 0, 0)
        return surf

    if tipo == "paso_virgen":
        surf = pygame.Surface((360, 260), pygame.SRCALPHA)
        PasoMacarena().dibujar(surf, 0, 0)
        return surf

    if tipo == "banda":
        surf = pygame.Surface((260, 140), pygame.SRCALPHA)
        Banda().dibujar(surf, 20, 20)
        return surf

    if tipo == "habito":
        surf = pygame.Surface((200, 260), pygame.SRCALPHA)
        HabitoNazareno(
            estado["color_tunica"],
            estado["color_capirote"],
            estado["color_cingulo"]
        ).dibujar(surf, 40, 20)
        return surf

    return pygame.Surface((100, 100))
