# __init__.py principal que expone todos los módulos del juego

# -------------------------
# CORE
# -------------------------
from .core.economia import (
    cargar_partida,
    guardar_partida,
    actualizar_bonus
)

from .core.hermandad import (
    DIAS_SALIDA,
    PUEBLOS,
    TIPOS_CRISTO,
    TIPOS_PASO,
    TIPOS_PALIO,
    TIPOS_BANDA
)

from .core.assets import (
    cargar_imagen,
    cargar_sonido
)

from .core.ui import (
    Boton
)

# -------------------------
# MENÚS
# -------------------------
from .menus.ajustes import (
    dibujar_ajustes,
    reiniciar_partida
)

from .menus.logros import (
    dibujar_logros,
    comprobar_logros
)

from .menus.hermanos import (
    dibujar_hermanos,
    añadir_hermano,
    baja_ultimo_hermano
)

from .menus.procesion import (
    dibujar_procesion,
    actualizar_procesion,
    reproducir_banda,
    parar_banda,
    reproducir_aplausos
)

# -------------------------
# SECCIONES
# -------------------------
from .secciones.gestion import dibujar_gestion
from .secciones.iglesia import dibujar_iglesia, donar, pedir_permiso
from .secciones.bandas import dibujar_bandas, crear_banda, contratar_banda, generar_ingresos_banda
from .secciones.mayordomia import dibujar_mayordomia
from .secciones.calendario import dibujar_calendario
from .secciones.habitos import dibujar_habito
from .secciones.cabildos import dibujar_cabildos, añadir_titulo, cambiar_nombre, cambiar_dia
from .secciones.cultos import dibujar_cultos, añadir_culto, añadir_ensayo, añadir_traslado
from .secciones.economia_avanzada import dibujar_economia, añadir_ingreso, añadir_gasto
from .secciones.semanasanta import dibujar_semanasanta

# -------------------------
# EXPORTACIÓN GLOBAL
# -------------------------
__all__ = [
    # CORE
    "cargar_partida", "guardar_partida", "actualizar_bonus",
    "DIAS_SALIDA", "PUEBLOS", "TIPOS_CRISTO", "TIPOS_PASO", "TIPOS_PALIO", "TIPOS_BANDA",
    "cargar_imagen", "cargar_sonido",
    "Boton",

    # MENÚS
    "dibujar_ajustes", "reiniciar_partida",
    "dibujar_logros", "comprobar_logros",
    "dibujar_hermanos", "añadir_hermano", "baja_ultimo_hermano",
    "dibujar_procesion", "actualizar_procesion", "reproducir_banda", "parar_banda", "reproducir_aplausos",

    # SECCIONES
    "dibujar_gestion",
    "dibujar_iglesia", "donar", "pedir_permiso",
    "dibujar_bandas", "crear_banda", "contratar_banda", "generar_ingresos_banda",
    "dibujar_mayordomia",
    "dibujar_calendario",
    "dibujar_habito",
    "dibujar_cabildos", "añadir_titulo", "cambiar_nombre", "cambiar_dia",
    "dibujar_cultos", "añadir_culto", "añadir_ensayo", "añadir_traslado",
    "dibujar_economia", "añadir_ingreso", "añadir_gasto",
    "dibujar_semanasanta",
]
