# # # Basic Import

# import turtle

# tim = turtle.Turtle()

# / # / # / # / # / #

# # # from... import...

# from turtle import *
# from random import *

# / # / # / # / # / #

# # # Aliasing Modules

# import turtle as t

# tim = t.Turtle()

# / # / # / # / # / #

# # # Installing Modules

# import heroes

# print(heroes.gen())

# / # / # / # / # / #

# from turtle import Turtle, Screen
# from random import randint, choice

# tim = Turtle()
# screen = Screen()

# tim.shape("circle")
# tim.shapesize(0.5)
# tim.color("red")
# tim.pencolor("black")

# / # / # / # / # / #

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# / # / # / # / # / #

# for _ in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# / # / # / # / # / #

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

# / # / # / # / # / #

# angles = [0, 90, 180, 270]
# screen.colormode(255)


# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     random_c = (r, g, b)
#     return random_c


# for _ in range(125):
#     tim.pencolor(random_color())
#     tim.width(10)
#     tim.speed(0)
#     direction = choice(angles)
#     tim.setheading(direction)
#     tim.forward(30)
#     tim.right(direction)

# / # / # / # / # / #

# screen.colormode(255)


# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     random_c = (r, g, b)
#     return random_c


# def circles(angle):
#     degrees = 0
#     tim.speed(0)
#     for _ in range(int(360 / angle)):
#         tim.circle(radius=100)
#         tim.pencolor(random_color())
#         tim.left(angle)
#         degrees += angle
#     print(int(360 / angle))


# circles(13.7)

# screen.exitonclick()

# / # / # PROJECT OF DAY 18 # / # / #

# import colorgram

# colors = colorgram.extract("image.jpg", 30)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
from random import choice

color_list = [(239, 214, 94), (219, 133, 164), (222, 73, 109), (13, 145, 98), (28, 131, 154),
              (136, 165, 191), (170, 50, 78), (10, 46, 69), (130, 193, 171), (26, 168, 124),
              (172, 24, 42), (169, 23, 16), (9, 164, 192), (165, 84, 46), (4, 110, 84),
              (236, 156, 176), (247, 212, 2), (208, 96, 65), (3, 97, 119), (160, 211, 194),
              (9, 61, 36), (60, 48, 28), (190, 181, 213), (73, 36, 62), (57, 54, 103)]

tim = turtle_module.Turtle()
screen = turtle_module.Screen()

screen.colormode(255)
screen.screensize(500, 500)
tim.hideturtle()
tim.penup()
tim.goto(-225, -215)
tim.speed(0)
my_x = tim.xcor()
my_y = tim.ycor()

for _ in range(10):
    for _ in range(11):
        if _ % 10 == 0 and _ != 0:
            tim.penup()
            my_y += 50
            tim.goto(my_x, my_y)
        else:
            tim.dot(20, choice(color_list))
            tim.penup()
            tim.forward(50)
            tim.pendown()

screen.exitonclick()
