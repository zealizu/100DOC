import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Set window size
screen.tracer(0)  # Turn off automatic screen updates for smoother animation
screen.listen()  # Listen for keyboard input

# Create game objects
player = Player()  # The player-controlled turtle
car_manager = CarManager()  # Manages all cars
score_board = Scoreboard()  # Displays the level and game over message

# Bind the "Up" arrow key to the player's move method
screen.onkeypress(player.move, "Up")

game_is_on = True  # Control variable for the main game loop
while game_is_on:
    time.sleep(0.1)  # Control the speed of the game loop
    screen.update()  # Update the screen with new positions

    # Randomly generate a car every few frames
    if random.randint(1, 6) == 1:
        car_manager.generate_car()

    car_manager.move_cars()  # Move all cars forward

    # Check if the player has reached the finish line
    if player.ycor() > 280:
        player.move_home()  # Reset player to starting position
        car_manager.increase_speed()  # Increase car speed for next level
        score_board.increase_level()  # Update the level display
    
    # Check for collision with any car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score_board.game_over()  # Display "GAME OVER"
            game_is_on = False  # End the game loop

screen.exitonclick()  # Keep the window open until clicked
