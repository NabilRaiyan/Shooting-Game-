from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x, y)
        self.score = 0

        self.update_score()


    # Update scoreboard
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT, align="center")

    # Increase scoreboard
    def score_increase(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))

