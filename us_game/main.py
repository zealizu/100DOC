from turtle import Turtle, Screen
import turtle
import pandas

screen = Screen()
screen.title("U.S States Game")
image = "100DOC/us_game/blank_states_img.gif"
screen.bgpic(image)
screen.tracer(0)
name = Turtle()
name.ht()

answer_state = screen.textinput(title= "Guess the State", prompt="What's another state name? ").title()
states = pandas.read_csv("100DOC/us_game/50_states.csv")
game_is_on = True
score = 0
guessed_states: list = []
all_states = states.state.to_list()

while game_is_on:
    screen.update()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("100DOC/us_game/need_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state = states[states.state == answer_state]
        x_cor = state.x.item()
        y_cor = state.y.item()
        name.pu()
        name.goto(float(x_cor), float(y_cor))
        name.write(answer_state)
        score += 1
    if score == 50:
        game_is_on = False
        
    answer_state = screen.textinput(title= f"{score}/50 States Correct", prompt="What's another state name? ").title()


