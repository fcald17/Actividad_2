#Importar elementos de librerías diferentes:
#Importar 'randrange' para cambiar la posición de la comida al azar y 'choice' para cambiar el color de la serpiente y comida
from random import randrange, choice
#Importar todos los elementos de la biblioteca gráfica 'turtle'
from turtle import *
#Importar 'square' para generar el visual de la comida y la serpiente y 'vector' para facilitar el uso de posiciones
from freegames import square, vector

#Generar la lista de 5 colores para la serpiente y comida
colors = ['blue', 'green', 'black', 'purple', 'yellow']
#Elegir dos colores al azar
choice_s = choice(colors)
choice_f = choice(colors)
#Bucle while para asegurarse de que ambos colores sean diferentes
while choice_s == choice_f:
    choice_f = choice(colors)

#Crear la comida
food = vector(0, 0)
#Crear la serpiente
snake = [vector(10, 0)]
#Darle dirección a la serpiente a través de vectores
aim = vector(0, -10)


#Función para el cambio de dirección de la serpiente
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

#Función para determinar si la cabeza de la serpiente sigue en los límites del juego
def inside(head):
    """Return True if head inside boundaries."""
    #Regresa las dos coordinadas de la cabeza de la serpiente
    return -200 < head.x < 190 and -200 < head.y < 190

#Función para el movimiento de la serpiente
def move():
    """Move snake forward one segment."""
    #Crea una copia de la última parte de la serpiente, la cabeza para evitar cambiar su posición dentro del cuerpo
    head = snake[-1].copy()
    #Genera el movimiento de la cabeza de la serpiente con el valor dado al vector de aim
    head.move(aim)

    #Se determina con la función 'inside' si la cabeza sigue en los límites o si colisiona con su propio cuerpo
    if not inside(head) or head in snake:
        #Si resulta en alguna de las dos condiciones, la cabeza se vuelve roja
        square(head.x, head.y, 9, 'red')
        #Se actualiza el visual del juego para mostrar que has perdido
        update()
        return

    #Hace la ilusión de movimiento junto con 'snake.pop(0)', pues da la ilusión de que se mueve al agregar un elemento al frente y elimar uno atrás
    snake.append(head)

    #Función para determinar si la serpiente ha comido
    if head == food:
        #Indica en la pantalla de comandos la longitud de la serpiente
        print('Snake:', len(snake))
        #Reubica la posición de la comida con nuevas coordinadas aleatorias
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        #Si no se come, se elimina la cola de la serpiente para dar la ilusión de movimiento, si esto no se hiciera, al agregar la cabeza con 'snake.append(head)', la serpiente crecería
        snake.pop(0)

    #El juego vuelve a dibujar la serpiente y la comida en sus nuevas posiciones
    clear()

    #Genera el cuerpo de la serpiente y lo colorea con el color aleatorio elegido al inicio
    for body in snake:
        square(body.x, body.y, 9, choice_s)

    #Dibuja la comida en su posición con el color aleatorio elegido al principio
    square(food.x, food.y, 9, choice_f)

    #Muestra todos los nuevos cambios hechos en los visuales
    update()
    #Determina que el bucle para que la serpiente se mueva cada 100 milisegundos y dé tiempo para cambiar su dirección si se presiona una tecla
    ontimer(move, 100)

#Genera la pantalla del juego, los primeros números, sus dimesiones, los últimos dos, su posición en la pantalla de la computadora
setup(420, 420, 370, 0)
#Oculta la tortuga que genera los gráficos
hideturtle()
#Evita que la pantalla se actualice automáticamente para ahorro de tiempo
tracer(False)
#Permite que el programa identifique si se ha presionado una tecla y recibir información al respecto
listen()
#Si se presionan las flechas, dependiendo de su dirección, cambia la dirección de la serpiente
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
#Después de cambiar su dirección, sigue su movimiento en esta nueva dirección
move()
#Pone la pantalla en bucle para que no se cierre con cada acción ejectada
done()
