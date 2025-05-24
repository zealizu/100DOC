from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]  # Possible car colors
STARTING_MOVE_DISTANCE = 5  # Initial speed of cars
MOVE_INCREMENT = 10  # How much the speed increases each level

class CarManager:
    def __init__(self):
        self.all_cars = []  # List to keep track of all car objects
        self.move_distance = STARTING_MOVE_DISTANCE  # Current speed of cars

    def generate_car(self):
        # Create a new car at the right edge with a random color and y-position
        new_car = Turtle("square")
        new_car.penup()
        new_car.setheading(180)  # Face left
        new_car.shapesize(stretch_wid=1.0, stretch_len=2.0)  # Make the car rectangle-shaped
        new_car.color(random.choice(COLORS))
        new_car.goto(280, random.randint(-250, 250))  # Start at right edge, random y
        self.all_cars.append(new_car)  # Add the new car to the list

    def move_cars(self):
        # Move all cars forward by the current move distance
        for car in self.all_cars:
            car.forward(self.move_distance)
            
    def increase_speed(self):
        # Increase the speed of the cars for the next level
        self.move_distance += MOVE_INCREMENT
