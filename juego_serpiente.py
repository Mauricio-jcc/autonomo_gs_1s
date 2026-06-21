
import time
import keyboard
import random
print ("Bienvenido al juego de la serpiente")
print ("Elige un modo: 1 Nueva partida, 2 Cargar Partida, 3 opciones, 4 Salir")
modo_elegido = int(input ("Por favor, seleccione el modo de juego:"))
if  modo_elegido == 1 : 
        print ("Inicia el juego")
elif modo_elegido == 2 : 
        print ("Selecciona tu partida")
elif modo_elegido == 3 : 
        print ("Cargando opciones")
elif modo_elegido == 4 : 
        print ("Saliendo del juego") 
    
time.sleep (3)
ancho = 10
alto = 10
serpiente = [[5, 5]]
direccion = [1, 0]
comida = [3, 3]


def cambiar_direccion():
    global direccion
    if keyboard.is_pressed("w"):
        direccion = [0, -1]
    elif keyboard.is_pressed("s"):
        direccion = [0, 1]
    elif keyboard.is_pressed("a"):
        direccion = [-1, 0]
    elif keyboard.is_pressed("d"):
        direccion = [1, 0]


while True:
    cambiar_direccion()

    nueva_pos_cabeza = [
        serpiente[-1][0] + direccion[0],
        serpiente[-1][1] + direccion[1],
    ]

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
        # Generar nuevas coordenadas para la comida
        comida = [random.randint(0, ancho - 1), random.randint(0, alto - 1)]
    else:
        serpiente.pop(0)

    for y in range(alto):
        linea = ""
        for x in range(ancho):
            if [x, y] in serpiente:
                linea += "S"
            elif [x, y] == comida:
                linea += "C"
            else:
                linea += "."
        print(linea)

    time.sleep(0.5)