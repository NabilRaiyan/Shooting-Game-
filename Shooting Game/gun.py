from turtle import Turtle
from barrel import Barrel


# Creating gun class
class Gun(Turtle):

    def __init__(self):
        self.bullets = []
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("orange")
        self.goto(0, -300)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.right = 20
        self.left = -20

        self.health = 5

        # Creating gun barrel
        self.barrel = Barrel()
        self.barrel.goto(self.xcor(), self.ycor() + 20)

    # Creating player bullet
    def create_bullet(self):
        bullet = Turtle()
        bullet.penup()
        bullet.color("orange")
        bullet.shape("square")
        bullet.goto(self.xcor(), self.ycor() + 10)
        bullet.setheading(90)
        bullet.shapesize(stretch_len=0.2, stretch_wid=0.1)
        self.bullets.append(bullet)

    # Player shooting method
    def shoot(self):
        for bullet in self.bullets:
            bullet.forward(20)

    # Player movement
    def move_right(self):
        new_x = self.xcor() + self.right
        self.goto(new_x, self.ycor())
        self.barrel.goto(new_x, self.barrel.ycor())

    def move_left(self):
        new_x = self.xcor() + self.left
        self.goto(new_x, self.ycor())
        self.barrel.goto(new_x, self.barrel.ycor())

    # Hide the gun while game is over
    def hide(self):
        self.hideturtle()
        self.barrel.hideturtle()
