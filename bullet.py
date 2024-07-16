# bullet.py

import turtle
from config import BULLET_SPEED

class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.hideturtle()
        self.speed = BULLET_SPEED
        self.state = "ready"

    def fire(self, player):
        if self.state == "ready":
            self.state = "fire"
            x = player.xcor()
            y = player.ycor() + 10
            self.goto(x, y)
            self.showturtle()

    def move(self):
        if self.state == "fire":
            y = self.ycor()
            y += self.speed
            self.sety(y)

        if self.ycor() > 275:
            self.hideturtle()
            self.state = "ready"
