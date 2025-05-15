from turtle import Turtle  # Import Turtle class for scoreboard graphics

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.color("white")  # Set text color to white
        self.pu()  # Lift the pen to avoid drawing lines
        self.ht()  # Hide the turtle cursor
        self.l_score = 0  # Initialize left player's score
        self.r_score = 0  # Initialize right player's score
        self.update()  # Display the initial scores

    def update(self):
        # Clear previous scores and write the updated scores at the top of the screen
        self.clear()
        self.goto(-100, 200)  # Position for left player's score
        self.write(f"{self.l_score}", align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)  # Position for right player's score
        self.write(f"{self.r_score}", align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        # Increment left player's score and update display
        self.l_score += 1
        self.update()

    def r_point(self):
        # Increment right player's score and update display
        self.r_score += 1
        self.update()