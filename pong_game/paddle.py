from turtle import Turtle  # Import Turtle class for paddle graphics

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()  # Initialize the Turtle superclass
        self.shape("square")  # Set paddle shape to square
        self.color("white")  # Set paddle color to white
        self.pu()  # Lift the pen to avoid drawing lines
        self.shapesize(5, 1)  # Stretch the square to make a paddle (5 tall, 1 wide)
        self.x_position = 350 * pos  # Set x position: 350 for right, -350 for left
        self.goto(self.x_position, 0)  # Place paddle at starting position

    def move_up(self):
        # Move the paddle up by 20 pixels, but not beyond the top edge
        if self.ycor() < 250:
            y_position = self.ycor() + 20
            self.goto(self.x_position, y_position)

    def move_down(self):
        # Move the paddle down by 20 pixels, but not beyond the bottom edge
        if self.ycor() > -250:
            y_position = self.ycor() - 20
            self.goto(self.x_position, y_position)