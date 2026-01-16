import os 
  
# ==== VARIABLES GLOBALES ====
lista_amigos = []      
lista_edades = []      

# ==== MOSTRAR AGENDA ====
def mostrarAmigosYEdades():
    """Muestra todos los amigos y sus edades"""
    # Si la agenda está vacía, avisamos
    if not lista_amigos:
        print("\nLa agenda está vacía\n")
    else:
        # Recorremos ambas listas a la vez y mostramos los datos
        print("\n--- AGENDA ---")
        for nombre, edad in zip(lista_amigos, lista_edades):
            print(nombre, "-", edad, "años")
        print()

# ==== AÑADIR AMIGOS ====
def añadirAmigos():
    """Añade amigos y sus edades a la lista. Enter para terminar."""
    while True:
        # Pedimos el nombre
        nombre = input("Nombre (Enter para terminar): ")
        # Si pulsa Enter sin escribir nada → salir del bucle
        if nombre == "":
            break
        # Pedimos la edad
        edad = input("Edad: ")
        # Guardamos los datos en las listas globales
        lista_amigos.append(nombre)
        lista_edades.append(edad)

# ==== GUARDAR AGENDA EN CSV ====
def guardarAgenda():
    """Guarda la agenda en un fichero CSV con formato nombre;edad"""
    # Abrimos el archivo en modo escritura
    with open("agenda.csv", "w", encoding="utf8") as f:
        # Guardamos cada amigo en una línea con formato nombre;edad
        for nombre, edad in zip(lista_amigos, lista_edades):
            f.write(nombre + ";" + edad + "\n")
    print("\nAgenda guardada en agenda.csv\n")

# ==== CARGAR AGENDA DESDE CSV ====
def cargarAgenda():
    """Carga la agenda desde el fichero CSV y cuenta los amigos"""
    # Comprobamos si el archivo existe
    if not os.path.exists("agenda.csv"):
        print("\nNo existe agenda.csv\n")
        return
    # Limpiamos las listas antes de cargar
    lista_amigos.clear()
    lista_edades.clear()
    # Leemos el archivo línea por línea
    with open("agenda.csv", "r", encoding="utf8") as f:
        for linea in f:
            # Separamos nombre y edad usando el ;
            nombre, edad = linea.strip().split(";")
            lista_amigos.append(nombre)
            lista_edades.append(edad)
    print(f"\nAgenda cargada. Total amigos: {len(lista_amigos)}\n")

# ==== MENÚ PRINCIPAL ====
while True:
    print("1. Añadir amigos")
    print("2. Mostrar agenda")
    print("3. Guardar agenda")
    print("4. Cargar agenda")
    print("5. Salir")
    
    opcion = input("Opción: ")
    if opcion == "1":
        añadirAmigos()
    elif opcion == "2":
        mostrarAmigosYEdades()
    elif opcion == "3":
        guardarAgenda()
    elif opcion == "4":
        cargarAgenda()
    elif opcion == "5":
        break
    else:
        print("Opción no válida\n")