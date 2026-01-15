import os

# Crear un directorio
os.mkdir("datos")

# Crear varios niveles de directorios y borrar nivel2
os.makedirs("nivel1/nivel2")
os.rmdir("nivel1/nivel2")

# Crear un archivo
with open("archivo_creado.txt", "w", encoding="utf8") as f:
    f.write("Este archivo ha sido creado desde el script.\n")

# Mover el archivo al directorio "datos"
if os.path.isdir("datos"):
    os.rename("archivo_creado.txt", "datos/archivo_creado.txt")

# Mostrar el directorio actual y path de archivo_creado
print("Directorio actual:", os.getcwd())
print("\nPath absoluto de archivo_creado.txt (si existe):")
print(os.path.abspath("datos/archivo_creado.txt"))

# Listar contenido de un directorio
if os.path.isdir("docs"):
    print("\nContenido de 'docs':")
    for f in os.listdir("docs"):
        print(f)

# Saber si es fichero o directorio
print("\nContenido del directorio actual:")
for f in os.listdir():
    if os.path.isfile(f):
        print(f"{f} es fichero")
    else:
        print(f"{f} es directorio")

# Leer un fichero de texto
try:
    f = open("datos/archivo_creado.txt", "rt", encoding="utf8")
    for linea in f.readlines():
        print(linea, end="")
    f.close()
except FileNotFoundError:
    print("\nNo se encontró notas.txt")