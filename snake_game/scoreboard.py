from turtle import Turtle  # Import the Turtle class

# Class to manage the scoreboard
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent Turtle class
        self.score = 0  # Initialize the score to 0
        with open("100DOC/snake_game/data.txt","r") as file:
            content = file.read()
        self.high_score = int(content)
        self.color("white")  # Set the text color to white
        self.ht()  # Hide the turtle cursor
        self.pu()  # Lift the pen to avoid drawing lines
        self.write_score()  # Display the initial score

    def write_score(self):
        """
        Clears the previous score and writes the updated score on the screen.
        """
        self.clear()  # Clear the previous score
        self.goto(0, 260)  # Move to the top center of the screen
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Arial', 30, 'bold'))  # Display the score

    def update_score(self):
        """
        Increments the score by 1 and updates the display.
        """
        self.score += 1  # Increment the score
        self.write_score()  # Update the score display
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("100DOC/snake_game/data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     """
    #     Displays the "Game Over" message on the screen.
    #     """
    #     self.goto(0, 0)  # Move to the center of the screen
    #     self.write("Game Over", align="center", font=('Arial', 30, 'normal'))  # Display "Game Over"
