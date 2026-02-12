# 📘 README.md — Proyecto MyCofradía Procesión

## 🎮 Descripción del proyecto

Este módulo del proyecto **MyCofradía** implementa un sistema completo de **procesión interactiva**, donde el usuario puede:

- Elegir **modo libre** o **modo procesión**
- Elegir entre **Cristo** o **Virgen**
- Controlar el paso con movimientos reales:
  - Racheado
  - Costero
  - Picaíto
  - Paso muda
  - Pasito
  - Tres pasos
  - Para atrás
  - Levantá
  - Levantá a la música
- Cámara suave
- Recorrido automático
- Panel lateral con controles
- Integración con el menú general de procesión

Todo está construido con **Pygame**.

---

## 📁 Estructura del proyecto
´text

mycofradia3/
│
├── main.py
├── config.py
├── assets/
│ └── img/
│ ├── fondo_procesion.png
│ ├── paso_cristo.png
│ ├── paso_virgen.png
│ ├── icono_procesion.png
│ ├── icono_enseres.png
│ ├── icono_ayuda.png
│ ├── icono_secretaria.png
│ ├── icono_tesoreria.png
│
├── core/
│ ├── botones.py
│ └── ui.py
│
└── modules/
└── menus/
├── procesion_menu.py
└── procesion.py
´´


---

## 📄 Descripción de cada archivo

### 🔹 `main.py`

Punto de entrada del juego.  
Carga la ventana principal y llama a los distintos menús, incluido el menú de procesión.

---

### 🔹 `config.py`

Contiene configuraciones globales, como:

- Colores
- Rutas
- Ajustes generales

El motor de procesión usa `COLORES`.

---

### 🔹 `core/botones.py`

Define la clase `BotonSimple`, usada en los menús.

---

### 🔹 `core/ui.py`

Funciones para dibujar:

- Títulos
- Paneles
- Textos

---

### 🔹 `modules/menus/procesion_menu.py`

Es el menú principal de la sección de procesión.

Incluye:

- Botón **“Iniciar procesión”**
- Botones para:
  - Itinerario
  - Cortejo
  - Meteorología
  - Horarios
  - Papeletas
- Carga de iconos
- Panel derecho con información
- Llamada a `menu_procesion_motor()` cuando el usuario inicia la procesión

⚠ Este archivo **no contiene el motor**, solo el menú.

---

### 🔹 `modules/menus/procesion.py`

Este archivo contiene **TODO el motor de la procesión**:

#### ✔ Selector de modo
- Libre
- Procesión

#### ✔ Selector de tipo
- Cristo
- Virgen

#### ✔ Motor completo
- Carga del mapa
- Carga del paso
- Cámara suave
- Recorrido automático
- Dibujo del paso
- Sombra
- Panel lateral

---

## ✝️ Andares del Cristo

- `1` → Siempre de frente  
- `2` → Racheado  
- `3` → Costero izq  
- `4` → Costero der  
- `5` → Para atrás  
- `6` → Picaíto  
- `7` → Paso muda  
- `8` → Pasito  
- `9` → Tres pasos  
- `0` → Pararse y bajar  
- `ESPACIO` → Levantá  
- `º` → Levantá a la música  

---

## 👑 Andares de la Virgen

- `1` → De frente  
- `2` → Para atrás  
- `3` → Mecida  
- `4` → Costero izq  
- `5` → Costero der  
- `ESPACIO` → Levantá  
- `º` → Levantá a la música  

---

## 🔄 Movimiento según el giro (revira real)

El paso se mueve en la dirección hacia donde está girado, usando **trigonometría real** para calcular el desplazamiento.

---

## 🖼️ Archivos PNG necesarios

Dentro de `assets/img/` deben existir:

| Archivo | Uso |
|----------|------|
| fondo_procesion.png | Fondo del mapa |
| paso_cristo.png | Imagen del paso de Cristo |
| paso_virgen.png | Imagen del paso de la Virgen |
| icono_procesion.png | Icono del menú “Itinerario” |
| icono_enseres.png | Icono del menú “Cortejo” |
| icono_ayuda.png | Icono del menú “Meteorología” |
| icono_secretaria.png | Icono del menú “Horarios” |
| icono_tesoreria.png | Icono del menú “Papeletas” |

Si alguno falta, el motor crea un **rectángulo de emergencia**.

---

## 🎮 Controles del motor

### ✝️ Cristo

- `1` → Siempre de frente  
- `2` → Paso racheado  
- `3` → Costero izq  
- `4` → Costero der  
- `5` → Para atrás  
- `6` → Picaíto  
- `7` → Paso muda  
- `8` → Pasito  
- `9` → Tres pasos  
- `0` → Pararse y bajar  
- `ESPACIO` → Levantá  
- `º` → Levantá a la música  
- `A / D` → Girar  

---

### 👑 Virgen

- `1` → De frente  
- `2` → Para atrás  
- `3` → Mecida  
- `4` → Costero izq  
- `5` → Costero der  
- `ESPACIO` → Levantá  
- `º` → Levantá a la música  
- `A / D` → Girar  

---

## 🚀 Cómo iniciar la procesión

1. En el menú de procesión, pulsa **Iniciar procesión**  
2. Elige modo  
3. Elige Cristo o Virgen  
4. Controla el paso con las teclas  

---

## 🛠️ Requisitos

- Python 3.x  
- Pygame  

Instalación de Pygame:

```bash
pip install pygame