from turtle import Turtle
FONT = ("Courier", 24, "normal")  # Font for displaying text

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1  # Start at level 1
        self.update_level()  # Display the initial level
        
    def update_level(self):
        # Clear previous text and write the current level at the top left
        self.clear()
        self.pu()
        self.ht()
        self.goto(-230, 260)
        self.color("black")
        self.write(arg= f"Level: {self.level}", align= "center", font = FONT)
    
    def increase_level(self):
        # Increase the level by 1 and update the display
        self.level += 1
        self.update_level()
    
    def game_over(self):
        # Display "GAME OVER" message in the center of the screen
        self.home()
        self.write(arg= f"GAME OVER", align= "center", font = FONT)
