# Simple pong game

import time  # Import time module for controlling game speed
from turtle import Screen  # Import Screen class for creating the game window
from paddle import Paddle  # Import Paddle class for player paddles
from ball import Ball  # Import Ball class for the ball
from scoreboard import ScoreBoard  # Import ScoreBoard class for keeping score

# Set up the game window
screen = Screen()
screen.setup(800, 600)  # Set window size to 800x600 pixels
screen.title("Pong Game")  # Set the window title
screen.bgcolor("black")  # Set background color to black
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Create the right and left paddles, the ball, and the scoreboard
r_paddle = Paddle(1)  # Right paddle at position 1 (right side)
l_paddle = Paddle(-1)  # Left paddle at position -1 (left side)
ball = Ball()  # Create the ball
scoreboard = ScoreBoard()  # Create the scoreboard

# Set up keyboard controls for both paddles
screen.listen()  # Listen for keyboard input
screen.onkeypress(fun = r_paddle.move_up, key = "Up")  # Right paddle up
screen.onkeypress(fun = r_paddle.move_down, key = "Down")  # Right paddle down
screen.onkeypress(fun = l_paddle.move_up, key = "w")  # Left paddle up
screen.onkeypress(fun = l_paddle.move_down, key = "s")  # Left paddle down

game_is_on = True  # Control variable for the main game loop

# Main game loop
while game_is_on:
    time.sleep(ball.move_speed)  # Control the speed of the ball
    screen.update()  # Update the screen with new positions
    ball.move()  # Move the ball

    # Detect collision with top or bottom wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles and bounce
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    
    # Detect if the ball goes past the right paddle (left player scores)
    if ball.xcor() > 380:
        ball.home()  # Reset ball to center
        scoreboard.l_point()  # Increment left player's score
    
    # Detect if the ball goes past the left paddle (right player scores)
    if ball.xcor() < -380:
        ball.home()  # Reset ball to center
        scoreboard.r_point()  # Increment right player's score

screen.exitonclick()  # Keep the window open until clicked