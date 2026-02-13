# Pygame – Instalación y Configuración

## 🛠️ Requisitos

- **Python 3.11** (compatible con Pygame)  
- **Pygame**

---

## 💾 Instalación Paso a Paso

### 1️⃣ Descargar Python

1. Descargar el instalador oficial de Python 3.11 para Windows 11 (64 bits):  
   [Python 3.11.3 – Windows installer](https://www.python.org/downloads/release/python-3113/)  

2. Ejecutar el instalador y marcar la casilla:  
   ☑ **Add Python 3.11 to PATH**  

3. Hacer clic en **Install Now** y completar la instalación.

---

###PASO 2 — Desactiva el alias del Microsoft Store

Si sigue saliendo el mensaje raro de Microsoft Store:

Ve a:
Configuración → Aplicaciones → Configuración avanzada de aplicaciones

Entra en:
Alias de ejecución de aplicaciones

Desactiva:

python.exe
python3.exe
7
----

### 3️⃣ Verificar instalación

Abrir **PowerShell** o **CMD** y escribir:

```bash
python --version

Si no funciona, usar:

```bash
py --version

Debe mostrar algo como:

Python 3.11.3

Agregar Python al PATH (si no funcionó)

Si python --version no funciona:

Abrir Configuración → Variables de entorno

Editar la variable Path del sistema

Agregar las rutas (ajustando tu usuario):

C:\Users\TU_USUARIO\AppData\Local\Programs\Python\Python311\
C:\Users\TU_USUARIO\AppData\Local\Programs\Python\Python311\Scripts\


Reiniciar la terminal y verificar nuevamente:

python --version

---

4️⃣ Instalar Pygame

Actualizar pip e instalar Pygame:

python -m pip install --upgrade pip
python -m pip install pygame


Si usas py en vez de python, reemplázalo en los comandos.

---

5️⃣ Verificar Pygame

Abrir Python en la terminal:

python


Luego dentro del intérprete:

import pygame
pygame.init()


Si no hay errores, la instalación fue exitosa ✅

▶️ Ejecutar tu juego

En la carpeta donde esté tu archivo main.py:

python main.py


Si falla, usar:

py main.py


Esto abrirá tu juego usando Pygame.