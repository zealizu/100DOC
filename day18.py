from turtle import Turtle, Screen
import turtle as t
import random

tim = Turtle()
t.colormode(255)
# timmy.shape("turtle")
tim.color("deep pink")
# timmy.width(10)
# timmy.fd(100)
# timmy.up()
# timmy.fd(10)
# timmy.down()
# timmy.fd(1)

#code to draw a simple square using turtle
# for _ in range(4):
#     tim.fd(100)
#     tim.left(90)
#code to draw a Dashed Lnie
# for _ in range(15):
#     tim.pd()
#     tim.fd(10)
#     tim.pu()
#     tim.fd(10)


#code to draw all shapes from triangle to decagon in random colors
# num_sides = 3
color =[
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "gray", "cyan", "magenta", "lime", "navy", "gold", "salmon","turquoise", "indigo", "violet", "coral"
]
# while num_sides < 11:
#     angle = 360/num_sides
#     for side in range(num_sides):
#         tim.fd(100)
#         tim.left(angle)
#     tim.color(random.choice(color))
#     num_sides += 1

#code for simulating a random walk
# directions = [0, 90, 180,270]
# tim.width(10)
# tim.speed(0)
# for _ in range(100):
#     red = random.randint(0,255)
#     green = random.randint(0,255)
#     blue = random.randint(0,255)
#     color_list = [red, green, blue]
#     color_tuple = tuple(color_list)
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(color_tuple)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
#draw a spirograph 
tim.speed(0)
for _ in range(72):
    tim.color(random_color())
    tim.circle(100)
    tim.left(5)

    




screen = Screen()
screen.exitonclick()