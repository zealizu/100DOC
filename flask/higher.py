from flask import Flask
import random

app = Flask(__name__)
random_num = random.randint(0, 9)
print(random_num)

@app.route("/")
def homepage():
    return"<h1>Guess a number between 0 and 9</h1>"\
        "<img src= 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXVzdTJleDk4bGlnczAxazI3NWhtbTB1OHI4MTNwcTIwenViYTZqdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pWO49XP9L7TxbgQVib/giphy.gif'/>"
        
@app.route("/<number>")
def get_number(number):
    number = int(number)
    if number > random_num:
        return "<h1>Too high, try again</h1>"\
        "<img src= 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExejBhcXp1eW55MDg3dW50NmRleDJ3cTRqc3N5eDQwY20xMXd6bm9iMCZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/YBHJyPCU9h1VewdaPZ/200w.webp'/>"
    elif number < random_num:
        return "<h1>Too low, Try again</h1>"\
        "<img src= 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExejBhcXp1eW55MDg3dW50NmRleDJ3cTRqc3N5eDQwY20xMXd6bm9iMCZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/fUQ4rhUZJYiQsas6WD/200w.webp'/>"
    else:
        return "<h1>You found me</h1>"\
        "<img src= 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExejBhcXp1eW55MDg3dW50NmRleDJ3cTRqc3N5eDQwY20xMXd6bm9iMCZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/26DOMeaD2gdGE44LK/100.webp'/>"
        

if __name__ == "__main__":
    #Rn app in debug mode to auto reload
    app.run(debug=True)