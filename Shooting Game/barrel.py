from turtle import Turtle


# Creating gun barrel
class Barrel(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=0.2, stretch_wid=2)
        self.goto(0, 0)
        self.color('orange')
