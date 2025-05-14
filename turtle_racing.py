#simple turtle racing game
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").strip().lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
startpoint = -100 
all_turtle = []
for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    startpoint += 30 
    new_turtle.goto(-230, startpoint)
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    for i in all_turtle:
        if i.xcor() < 230:
            i.fd(random.randint(0,10))
        else:
            winner = i.color()
            is_race_on = False
            break
if user_bet == winner[0]:
    print(f"{winner[0]} Won, You won the bet")
else:
    print(f"{winner[0].title()} Won, You lost the bet")

screen.bye()
    
