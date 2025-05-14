from turtle import Turtle  # Import the Turtle class

# Constants for snake movement
MOVE_DISTANCE = 20  # Distance the snake moves in one step
UP = 90  # Angle for moving up
DOWN = 270  # Angle for moving down
LEFT = 180  # Angle for moving left
RIGHT = 0  # Angle for moving right

# Class to manage the snake
class Snake:
    def __init__(self):
        self.snake_body = []  # List to store the segments of the snake
        self.position = 0  # Initial position of the snake
        self.create_snake()  # Create the initial snake with 3 segments

    def create_snake(self):
        """
        Creates the initial snake with 3 segments.
        """
        for i in range(3):  # Create 3 segments
            segment = Turtle("square")  # Create a square-shaped segment
            segment.pu()  # Lift the pen to avoid drawing lines
            segment.setx(self.position)  # Set the x-coordinate of the segment
            segment.color("white")  # Set the color of the segment to white
            self.position -= 20  # Move the next segment to the left
            self.snake_body.append(segment)  # Add the segment to the snake body

    def move(self):
        """
        Moves the snake forward by updating the position of each segment.
        """
        for i in range(len(self.snake_body) - 1, 0, -1):  # Start from the tail and move towards the head
            self.pos = self.snake_body[i - 1].position()  # Get the position of the previous segment
            self.snake_body[i].goto(self.pos)  # Move the current segment to the position of the previous segment
        self.snake_body[0].fd(MOVE_DISTANCE)  # Move the head forward

    def move_up(self):
        """
        Changes the snake's direction to up if it's not currently moving down.
        """
        if self.snake_body[0].heading() != DOWN:  # Prevent the snake from moving in the opposite direction
            self.snake_body[0].setheading(UP)

    def move_down(self):
        """
        Changes the snake's direction to down if it's not currently moving up.
        """
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def move_left(self):
        """
        Changes the snake's direction to left if it's not currently moving right.
        """
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def move_right(self):
        """
        Changes the snake's direction to right if it's not currently moving left.
        """
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def has_eaten(self):
        """
        Adds a new segment to the snake when it eats food.
        """
        segment = Turtle("square")  # Create a new square-shaped segment
        segment.pu()  # Lift the pen to avoid drawing lines
        segment.color("white")  # Set the color of the segment to white
        self.snake_body.append(segment)  # Add the new segment to the snake body
