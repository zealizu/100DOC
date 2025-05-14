###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from turtle import Turtle, Screen
import turtle as t
import random
t.colormode(255)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

# print(rgb_colors)

tim = Turtle()
tim.teleport(-340,-310)
tim.width(30)
tim.speed("fastest")
end_screen = False
def move_turtle(degree):
        tim.pd()
        tim.fd(1)
        tim.setheading(90)
        tim.pu()
        tim.fd(50)
        tim.pd()
        tim.setheading(degree)
def generate_color():
    return random.choice(rgb_colors)

tim.color(generate_color())
while tim.ycor() < 300:
    tim.pd()
    tim.fd(1)
    tim.pu()
    tim.fd(50)
    tim.color(generate_color())
    if tim.xcor() > 300:
        move_turtle(180)
        end_screen = True
    elif tim.xcor() < -300 and end_screen:
        move_turtle(360)
        end_screen = False





screen = Screen()
screen.exitonclick()