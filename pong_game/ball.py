# Ball section of the code
from turtle import Turtle  # Import Turtle class for ball graphics

class Ball(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.shape("circle")  # Set ball shape to circle
        self.color("white")  # Set ball color to white
        self.pu()  # Lift the pen to avoid drawing lines
        self.x_move = 10  # Set initial movement in x direction
        self.y_move = 10  # Set initial movement in y direction
        self.move_speed = 0.1  # Set initial speed of the ball

    def move(self):
        # Move the ball by its current x and y increments
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        # Reverse the y direction (bounce off top/bottom)
        self.y_move *= -1

    def bounce_x(self):
        # Reverse the x direction (bounce off paddle) and speed up
        self.x_move *= -1
        self.move_speed *= 0.9  # Increase speed after each paddle hit

    def home(self):
        # Reset the ball to the center and reset speed, then reverse direction
        super().home()
        self.move_speed = 0.1
        self.bounce_x()