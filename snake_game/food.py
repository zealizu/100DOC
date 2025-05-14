from turtle import Turtle  # Import the Turtle class
import random  # Import the random module for generating random positions

# Class to manage the food
class Food(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent Turtle class
        self.shape("turtle")  # Set the shape of the food to a circle
        self.pu()  # Lift the pen to avoid drawing lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Scale down the size of the food
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the speed of the food to the fastest
        self.refresh()  # Place the food at a random position

    def refresh(self):
        """
        Moves the food to a new random position on the screen.
        """
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate
        self.goto(random_x, random_y)  # Move the food to the new position
