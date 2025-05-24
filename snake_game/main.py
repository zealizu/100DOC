# Simple snake game
from turtle import Screen  # Import the Screen class from the turtle module
import time  # Import the time module for adding delays
from snake import Snake  # Import the Snake class
from food import Food  # Import the Food class
from scoreboard import ScoreBoard  # Import the ScoreBoard class

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Set the screen size to 600x600 pixels
screen.bgcolor("black")  # Set the background color to black
screen.title("My Snake Game")  # Set the title of the game window

screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Create instances of Snake, Food, and ScoreBoard
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.update()  # Update the screen to show the initial state

# Game loop control variable
game_is_on = True

# Set up key listeners for controlling the snake
screen.listen()
screen.onkeypress(fun=snake.move_up, key="Up")  # Move the snake up when the "Up" key is pressed
screen.onkeypress(fun=snake.move_left, key="Left")  # Move the snake left when the "Left" key is pressed
screen.onkeypress(fun=snake.move_down, key="Down")  # Move the snake down when the "Down" key is pressed
screen.onkeypress(fun=snake.move_right, key="Right")  # Move the snake right when the "Right" key is pressed

# Main game loop
while game_is_on:
    time.sleep(0.1)  # Add a delay to control the speed of the game
    snake.move()  # Move the snake
    screen.update()  # Update the screen to reflect the new state

    # Detect collision with food
    if snake.snake_body[0].distance(food) < 15:  # Check if the snake's head is close to the food
        food.refresh()  # Move the food to a new random location
        snake.has_eaten()  # Add a new segment to the snake
        scoreboard.update_score()  # Update the score

    # Detect collision with the snake's own body
    for i in range(1, len(snake.snake_body)):  # Loop through all segments except the head
        if snake.snake_body[0].distance(snake.snake_body[i]) < 15:  # Check if the head collides with a segment
            scoreboard.reset()
            snake.reset()

    # Detect collision with the wall
    if (
        snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -280 or
        snake.snake_body[0].ycor() > 280 or snake.snake_body[0].ycor() < -280
    ):
        scoreboard.reset()
        snake.reset()

screen.exitonclick()  # Close the game window when clicked