# import turtle

# tim = turtle.Turtle()

# / # / # / # / # / #

# from turtle import *
# from random import *

# / # / # / # / # / #

# import turtle as t

# tim = t.Turtle()

# / # / # / # / # / #

# import heroes

# print(heroes.gen())

# / # / # / # / # / #

from turtle import Turtle, Screen
from random import randint, choice

tim = Turtle()
screen = Screen()

tim.shape("circle")
tim.shapesize(0.5)
tim.color("red")
tim.pencolor("black")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# sides = 3
# screen.colormode(255)
#
# while sides <= 10:
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(360 / sides)
#     sides += 1
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     tim.pencolor(r, g, b)

angles = [0, 90, 180, 270]
screen.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_c = (r, g, b)
    return random_c


for _ in range(125):
    tim.pencolor(random_color())
    tim.width(10)
    tim.speed(0)
    direction = choice(angles)
    tim.setheading(direction)
    tim.forward(30)
    tim.right(direction)


screen.exitonclick()
