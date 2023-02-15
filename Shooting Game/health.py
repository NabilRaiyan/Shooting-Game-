from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Health(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x, y)
        self.health = 5
        self.update_health()

        # Gun health

    def update_health(self):
        self.clear()
        self.write(f"Health: {self.health}", font=FONT, align="center")

        # Decrease health

    def health_decrease(self):
        self.health -= 1

        self.update_health()

