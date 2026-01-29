# ✝️ MyCofradía 3

Simulador cofrade completo desarrollado en **Python + Pygame**, centrado en la gestión integral de una hermandad: economía, cultos, bandas, mayordomía, cabildos y una Semana Santa completa, con modo oscuro/claro, animaciones, sonidos cofrades e integración de imágenes reales.

---

## 🎮 Características

- Gestión completa de hermandad
- Sistema de hermanos con cuotas, cargos y devoción 
- Sistema de logros con recompensas 
- Economía avanzada con ingresos, gastos e historial 
- Cultos, ensayos y traslados 
- Bandas propias y contratadas 
- Mayordomía de Cristo y Virgen 
- Hábitos personalizables 
- Calendario cofrade 
- Semana Santa completa 
- Modo procesión interactivo 
- Modo oscuro / claro 
- Sonidos cofrades 
- Animaciones opcionales 
- Guardado automático 
- Arquitectura modular profesional

---

## 📁 Estructura del proyecto

```text
├── main.py
├── readme.md
│
├── data/
│   ├── save.json
│   │
│   ├── images/
│   │   ├── bandas/
│   │   ├── cristos/
│   │   ├── escudos/
│   │   ├── palios/
│   │   └── pasos/
│   │
│   └── sounds/
│
└── modules/
    ├── __init__.py
    │
    ├── core/
    │   ├── assets.py
    │   ├── economia.py
    │   ├── hermandad.py
    │   └── ui.py
    │
    ├── menus/
    │   ├── ajustes.py
    │   ├── hermanos.py
    │   ├── logros.py
    │   └── procesion.py
    │
    └── secciones/
        ├── bandas.py
        ├── cabildos.py
        ├── calendario.py
        ├── cultos.py
        ├── economia_avanzada.py
        ├── gestion.py
        ├── habitos.py
        ├── iglesia.py
        ├── mayordomia.py
        └── semanasanta.py
```

---

## 🧠 Descripción de archivos

### `main.py`
Archivo principal del juego. Controla:  
- Bucle de Pygame  
- Estados y navegación  
- Modo oscuro / claro  
- Animaciones  
- Sonidos  
- Guardado automático  
- Acceso a todas las pantallas  
- Integración del modo procesión  

---

## 📦 Módulos


### 🟪 Carpeta `core/`

**`economia.py`**  
- Carga y guardado de `save.json`  
- Bonus automático cada 2 horas  
- Estructura inicial de partida  
- Compatibilidad con partidas antiguas  

**`hermandad.py`**  
Base de datos interna:  
- Días de salida  
- Pueblos  
- Tipos de Cristo, paso, palio y banda  

**`ui.py`**  
- Clase `Boton`  
- Dibujado y detección de clics  

**`assets.py`**  
- Carga de imágenes reales  
- Carga de sonidos cofrades  
- Funciones: `cargar_imagen()`, `cargar_sonido()`  

---

### 🟦 Carpeta `menus/`

**`ajustes.py`**  
- Modo oscuro / claro  
- Activar/desactivar animaciones y sonidos  
- Volúmenes internos  
- Reinicio de partida  

**`logros.py`**  
- Sistema de logros con recompensas  
- Logros de prestigio, economía, cultos, hermanos, etc.  
- Pantalla de logros  

**`hermanos.py`**  
- Generación de hermanos  
- Cuotas, cargos, devoción y estado  
- Ingresos automáticos por cuotas  
- Alta y baja de hermanos  
- Listado y estadísticas  

**`procesion.py`**  
- Modo procesión completo  
- Animación del paso  
- Mecida, avance y parada  
- Banda sonora, aplausos  
- Nazarenos y público  
- Eventos visuales  

---

### 🟩 Carpeta `secciones/`

**`gestion.py`**  
- Día de salida, pueblo  
- Cristo, paso, palio y banda  
- Escudo y datos principales  

**`iglesia.py`**  
- Donaciones  
- Solicitud de permiso al obispo  
- Prestigio  
- Estado del permiso  

**`bandas.py`**  
- Crear banda propia  
- Contratar bandas externas  
- Contratos activos  
- Ingresos automáticos  

**`mayordomia.py`**  
- Vestimenta del Cristo y la Virgen  
- Mantos, coronas, túnicas y potencias  
- Imágenes reales  

**`calendario.py`**  
- Días importantes  
- Salidas oficiales y extraordinarias  

**`habitos.py`**  
- Colores de túnica, capa, cíngulo y capirote  
- Dibujo del hábito  

**`cabildos.py`**  
- Añadir títulos  
- Cambiar nombre de la hermandad  
- Votación del día de salida  
- Historial de cabildos  

**`cultos.py`**  
- Cultos, ensayos, traslados  
- Aumento de prestigio  
- Sonidos de culto  

**`economia_avanzada.py`**  
- Ingresos y gastos manuales  
- Balance total  
- Historial de movimientos  
- Colores verde / rojo  

**`semanasanta.py`**  
- Semana Santa completa  
- Domingo de Ramos a Domingo de Resurrección  
- Colores según tipo de salida  
- Identificación de hermandad, banda y salidas extraordinarias  

---

## 💾 Guardado

El archivo `data/save.json` almacena:  
- Dinero, Prestigio, Permiso del obispo  
- Datos de hermandad  
- Hábitos y Mayordomía  
- Cultos, ensayos y traslados  
- Economía avanzada  
- Bandas y contratos, Banda propia  
- Títulos y Historial de cabildos  
- Hermanos, Logros  
- Ajustes  

---

## 🎮 Controles

### General
- `M` → Modo oscuro / claro  
- `Clic` → Navegación  

### Gestión
- `← / →` → Cambiar día  
- `A / D` → Cambiar pueblo  
- `1–8` → Cambiar Cristo, paso, palio y banda  

### Iglesia
- `D` → Donar  
- `P` → Pedir permiso  

### Bandas
- `B` → Crear banda  
- `C` → Contratar banda  

### Mayordomía
- `1–8` → Cambiar vestimentas  

### Hábitos
- `1–8` → Cambiar colores  

### Cabildos
- `T` → Añadir título  
- `N` → Cambiar nombre  
- `C` → Cambiar día  

### Cultos
- `C` → Añadir culto  
- `E` → Añadir ensayo  
- `T` → Añadir traslado  

### Economía
- `I` → Añadir ingreso  
- `G` → Añadir gasto  

### Hermanos
- `H` → Añadir hermano  
- `B` → Dar de baja al último hermano  

### Procesión
- `A` → Avanzar  
- `S` → Parar  
- `M` → Mecida  
- `P` → Aplausos  

---

## 🏁 Estado del proyecto

✅ Juego funcional  
✅ Sistema modular profesional  
✅ Modo oscuro / claro  
✅ Animaciones  
✅ Sonidos cofrades  
✅ Imágenes reales  
✅ Economía avanzada  
✅ Cultos, ensayos y traslados  
✅ Semana Santa completa  
✅ Sistema de hermanos  
✅ Sistema de logros  
✅ Modo procesión  
✅ Guardado automático  