from turtle import Turtle
STARTING_POSITION = (0, -280)  # Where the player starts
MOVE_DISTANCE = 10  # How far the player moves with each key press
FINISH_LINE_Y = 280  # Y-coordinate for the finish line


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.move_home()  # Set up the player at the starting position
    
    def move(self):
        # Move the player forward by MOVE_DISTANCE
        self.fd(MOVE_DISTANCE)
    
    def move_home(self):
        # Reset the player to the starting position and set appearance
        self.shape("turtle")
        self.pu()  # Lift the pen to avoid drawing lines
        self.setheading(90)  # Face upwards
        self.goto(STARTING_POSITION)
