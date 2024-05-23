import random
from turtle import Turtle, Screen

colors = [(43, 105, 171), (233, 206, 116), (225, 152, 87), (183, 50, 77), (118, 87, 50), (228, 120, 147), (214, 61, 80), (109, 110, 188), (130, 175, 210), (115, 185, 139), (55, 176, 110), (116, 168, 37), (202, 18, 42), (33, 56, 113), (221, 61, 50), (26, 142, 108), (154, 222, 193), (181, 170, 221), (30, 163, 170), (84, 35, 39), (40, 46, 80), (233, 167, 180), (237, 172, 162), (76, 40, 39), (154, 208, 221), (115, 46, 43)]

def get_random_color():
    return random.choice(colors)
screen = Screen()
screen.colormode(255)

def draw():
    turtle = Turtle()
    
    ROWS, COLS = 10, 10
    print(turtle.position())
    turtle.penup()
    turtle.goto(-240, -250)
    for _ in range(ROWS):
        for _ in range(COLS):
            turtle.pendown()
            turtle.color(get_random_color())
            turtle.dot(30)
            turtle.penup()
            turtle.forward(60)
        turtle.setposition(-240, turtle.position()[1] + 60)
            
            
            
            
    
    
    
draw()
screen.exitonclick()




    