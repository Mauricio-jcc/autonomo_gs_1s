
import time
import keyboard
import random

# =====================================================================
# CONFIGURACIÓN Y VARIABLES GLOBALES
# =====================================================================
ancho = 20
alto = 10
serpiente = [[5, 5]]
direccion = [1, 0]
comida = [2, 1]
velocidad_espera = 0.5
puntuacion = 0

# Obstáculos
obstaculos = []
numero_obstaculos = 5
for _ in range(numero_obstaculos):
    obstaculos.append([random.randint(0, ancho - 1), random.randint(0, alto - 1)])

# Controles predeterminados
controles = {
     "arriba": "w",
     "abajo": "s",
     "izquierda": "a",
     "derecha": "d"
}

# =====================================================================
#  FUNCIONES DEL SISTEMA (GUARDAR/CARGAR)
# =====================================================================
def cargar_partida():
    global serpiente, comida, puntuacion
    try:
        archivo = open("partida.txt", "r")
        contenido = archivo.read()
        archivo.close()
        datos = eval(contenido)

        serpiente = datos["serpiente"]
        comida = datos["comida"]
        puntuacion = datos["puntuacion"]
        return datos
    except FileNotFoundError:
          print("No se encontro partida guardada")
          return None

def guardar_partida(puntuacion, serpiente, comida):
     datos = {
        "puntuacion": puntuacion,
        "serpiente": serpiente,
        "comida": comida
     }
     archivo = open("partida.txt", "w")
     archivo.write(str(datos))
     archivo.close()
     print("Partida guardada correctamente")

def cambiar_opciones():
     global velocidad_espera
     while True:
        print("Menú de Opciones")
        print("1. Cambiar tecla para subir")
        print("2. Cambiar tecla para bajar")
        print("3. Cambiar tecla para ir a la izquierda")
        print("4. Cambiar tecla para ir a la derecha")
        print("5. Seleccionar la dificultad")
        print("6. Volver al menu principal")

        eleccion = input("Selecciona una opción: ")
        if eleccion in ["1", "2", "3", "4"]:
            acciones = ["arriba", "abajo", "izquierda", "derecha"]
            accion = acciones[int(eleccion)-1]

            print(f"Presiona la nueva tecla para {accion}...")
            while True:
                if keyboard.read_key():
                    nueva_tecla = keyboard.read_key()
                    controles[accion] = nueva_tecla
                    print(f"Tecla para {accion} cambiada a: {nueva_tecla}")
                    time.sleep(1)
                    break
        elif eleccion == "5":
            print ("Selecciona la dificultad:")
            print ("1. Facil")
            print ("2. Intermedio")
            print ("3. Dificil")
            dif_eleccion = input("Selecciona una opcion:")
            if dif_eleccion == "1":
                velocidad_espera = 0.8
                print ("Velocidad cambiada a Facil")
            elif dif_eleccion == "2":
                velocidad_espera = 0.5
                print ("Velocidad cambiada a Intermedio")
            elif dif_eleccion == "3":
                velocidad_espera = 0.2
                print ("Velocidad cambiada a dificil")
            
        elif eleccion == "6":
            print("Regresando...")
            break
        else:
            print("Opción no valida. Intentalo de nuevo")

# =====================================================================
#  MENU PRINCIPAL DEL JUEGO
# =====================================================================
while True:
    print("\nBienvenido al juego de la serpiente")
    print("Elige un modo: 1 Nueva partida, 2 Cargar Partida, 3 opciones, 4 Salir")

    modo_elegido = int(input("Por favor, seleccione el modo de juego: "))
    if modo_elegido == 1: 
        print("Inicia el juego")
        break  
    elif modo_elegido == 2: 
        print("Cargando tu partida")
        cargar_partida()
        break  
    elif modo_elegido == 3: 
        print("Cargando opciones")
        cambiar_opciones()
    elif modo_elegido == 4: 
        print("Saliendo del juego")
        exit()
    else:
        print("Opción no valida en el menu principal")
            
time.sleep(1.5)

# =====================================================================
#  FUNCION PARA CAMBIAR DE DIRECCION A LA SERPIENTE
# =====================================================================
def cambiar_direccion():
    global direccion 
    if keyboard.is_pressed(controles["arriba"]):
        direccion = [0, -1]
    elif keyboard.is_pressed(controles["abajo"]):
        direccion = [0, 1]
    elif keyboard.is_pressed(controles["izquierda"]):
        direccion = [-1, 0]
    elif keyboard.is_pressed(controles["derecha"]):
        direccion = [1, 0]
    elif keyboard.is_pressed("g"):
         guardar_partida(puntuacion, serpiente, comida)

# =====================================================================
# BUCLE PRINCIPAL DEL JUEGO 
# =====================================================================
while True:
    cambiar_direccion()

    nueva_pos_cabeza = [
        serpiente[-1][0] + direccion[0], 
        serpiente[-1][1] + direccion[1],
    ] 
    if nueva_pos_cabeza in obstaculos:
        print("¡Game Over!")
        break
    if nueva_pos_cabeza in serpiente:
        print("¡Game Over!")
        break
    if (
        nueva_pos_cabeza[0] < 0
        or nueva_pos_cabeza[0] >= ancho
        or nueva_pos_cabeza[1] < 0
        or nueva_pos_cabeza[1] >= alto
    ):
        print("¡Game Over!")
        break

    serpiente.append(nueva_pos_cabeza) 

    if nueva_pos_cabeza == comida:
        puntuacion += 15
        nueva_comida = [random.randint(0, ancho - 1), random.randint(0, alto - 1)]
        if nueva_comida not in serpiente and nueva_comida not in obstaculos:
            comida = nueva_comida
    else:
        serpiente.pop(0) 

    for y in range(alto):
        linea = "" 
        for x in range(ancho): 
            if [x, y] == serpiente[-1]:
                linea += "O"
            elif [x, y] in serpiente:
                linea += "S"
            elif [x, y] == comida:
                linea += "C"
            elif [x, y] in obstaculos:
                linea += "X"
            else:
                linea += "."
        print(linea)
        
    print("-----------------------------")
    print(f"Puntuación: {puntuacion}")
    print("-----------------------------")

    time.sleep(velocidad_espera)