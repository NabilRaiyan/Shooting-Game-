from turtle import Screen
from gun import Gun
from enemy import Enemy
import time
from scoreboard import Scoreboard
from health import Health

# Creating objects and animate screen
screen = Screen()
screen.listen()
screen.tracer(0)
gun = Gun()
enemy = Enemy()
score = Scoreboard(-240, 300)
health = Health(240, 300)

# Screen setup
screen.setup(width=700, height=700)
screen.title("Gun Game")
screen.bgcolor("black")

# Key functionality for player
screen.onkey(key="Right", fun=gun.move_right)
screen.onkey(key="Left", fun=gun.move_left)

game_is_on = True

# Game loop
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Gun shooting
    screen.onkey(key="s", fun=gun.create_bullet)
    gun.shoot()

    # Enemy shooting
    enemy.create_enemy()
    enemy.move_forward()
    enemy.shoot_enemy()

    # Detect collision of bullet with enemy
    for bullet in gun.bullets:
        for e in enemy.enemys:
            if bullet.distance(e) < 20:
                enemy.enemys.remove(e)
                e.hideturtle()
                score.score_increase()

    # Detecting collision enemy bullet with player
    for bullet in enemy.enemy_bullet:
        if bullet.distance(gun) < 30 and bullet.ycor() < -318:
            health.health_decrease()
            if health.health == 0:
                game_is_on = False
                score.game_over()

    # Detect collision of enemy with player
    for e in enemy.enemys:
        if e.distance(gun) < 50 and e.ycor() < -310:
            game_is_on = False
            score.game_over()


screen.exitonclick()
