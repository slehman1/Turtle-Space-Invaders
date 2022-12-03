from turtle import Turtle
font = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.hideturtle()
        self.penup()
        self.goto(0, 290)
        self.write("Score: 0 | Lives: 3", font=font, align="center")

    def update_scoreboard(self, new_score, new_lives):
        self.clear()
        self.write(f"Score: {new_score} | Lives: {new_lives}", font=font, align="center")

    def game_over(self, score):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over! You ran out of lives! Your score was {score}!", font=font, align="center")

    def win(self, score):
        self.clear()
        self.goto(0, 0)
        self.write(f"You win! Your score was {score}!", font=font, align="center")


