"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
from freegames import square, vector
import time 

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

last_food_time = time.time()

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def spawn_food():
    while True:
        food.x=randrange(-19,19)*10
        food.y=randrange(-19,19)*10
        if inside(food) and food not in snake:
            return

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    global last_food_time
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        spawn_food()
        last_food_time = time.time()
    else:
        snake.pop(0)
        if time.time() - last_food_time >= 5:
            spawn_food()
            last_food_time = time.time()

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
spawn_food()
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
