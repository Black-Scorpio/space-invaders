# alien.py

import turtle
from config import ALIEN_SPEED, ALIEN_DROP_SPEED

class Alien(turtle.Turtle):
    def __init__(self, start_x, start_y):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(start_x, start_y)
        self.alien_speed = ALIEN_SPEED

    def move(self, aliens):
        x = self.xcor()
        x += self.alien_speed
        self.setx(x)

        if self.xcor() > 380 or self.xcor() < -380:
            self.alien_speed *= -1  # Reverse the direction
            for alien in aliens:
                y = alien.ycor()
                y -= ALIEN_DROP_SPEED
                alien.sety(y)
