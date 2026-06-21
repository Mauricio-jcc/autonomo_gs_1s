
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
        exit()
        
    
time.sleep (3)
ancho = 10
alto = 10
serpiente = [[5, 5]]
direccion = [1, 0]
comida = [3, 3]

#Aqui desarrollamos el movimiento de la serpiente
def cambiar_direccion():
    global direccion #Se utiliza global para indicarle a python que se esta cambiando la variable global y no la local dentro de la funcion
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
    ] #Utiliza el ultimo dato agregado a la lista serpiente en funcion de la dirección
#Verifica que la serpiente no salga de los limites de la cuadricula
    if (
        nueva_pos_cabeza[0] < 0
        or nueva_pos_cabeza[0] >= ancho
        or nueva_pos_cabeza[1] < 0
        or nueva_pos_cabeza[1] >= alto
    ):
        print("¡Game Over!")
        break

    serpiente.append(nueva_pos_cabeza) #Añade un nuevo valor a la lista serpiente

    if nueva_pos_cabeza == comida:
        
        comida = [random.randint(0, ancho - 1), random.randint(0, alto - 1)] #Generacion de comida en un lugar ramdom de la cuadricula
    else:
        serpiente.pop(0) #Para que la serpiente avance sin cambiar de tamaño mientras no come

    for y in range(alto):
        linea = "" #Esta linea sirve para "dibujar" la cuadricula de forma vertical
        for x in range(ancho): #Esta linea sirve para visualizar la serpiente, la comida, y rellenar la cuadricula
            if [x, y] in serpiente:
                linea += "S"
            elif [x, y] == comida:
                linea += "C"
            else:
                linea += "."
        print(linea)

    time.sleep(0.5)