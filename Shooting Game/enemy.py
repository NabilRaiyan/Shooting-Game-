from turtle import Turtle
import random


# Creating enemy class
class Enemy:
    def __init__(self):
        self.enemys = []
        self.enemy_bullet = []

    # Creating enemy
    def create_enemy(self):
        if random.randint(1, 10) == 2 or random.randint(1, 10) == 1:
            self.enemy = Turtle()
            self.enemy.penup()
            self.enemy.setheading(270)
            self.enemy.shape("turtle")
            self.enemy.color("cyan")
            self.enemy.goto(random.randint(-300, 300), random.randint(240, 350) + 5)
            self.enemys.append(self.enemy)

            self.create_bullet(self.enemy.xcor(), self.enemy.ycor())

    # Enemy movement
    def move_forward(self):
        for enemy in self.enemys:
            enemy.forward(random.randint(1, 5))

    # Creating enemy bullet
    def create_bullet(self, x, y):
        bullet = Turtle("square")
        bullet.shapesize(stretch_len=0.1, stretch_wid=0.1)
        bullet.penup()
        bullet.color("cyan")
        bullet.goto(x, y)

        self.enemy_bullet.append(bullet)

    # Enemy shooting
    def shoot_enemy(self):

        for bullet in self.enemy_bullet:
            bullet.setheading(270)
            bullet.forward(10)
