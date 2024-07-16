# player.py

import turtle
from config import PLAYER_SPEED

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.goto(0, -250)
        self.speed = PLAYER_SPEED
        self.moving_left = False
        self.moving_right = False

    def move_left(self):
        if self.moving_left:
            x = self.xcor()
            x -= self.speed
            if x < -380:
                x = -380
            self.setx(x)

    def move_right(self):
        if self.moving_right:
            x = self.xcor()
            x += self.speed
            if x > 380:
                x = 380
            self.setx(x)

    def start_moving_left(self):
        if not self.moving_left:
            self.moving_left = True
            self.continuous_move_left()

    def continuous_move_left(self):
        if self.moving_left:
            self.move_left()
            turtle.ontimer(self.continuous_move_left, 50)

    def stop_moving_left(self):
        self.moving_left = False

    def start_moving_right(self):
        if not self.moving_right:
            self.moving_right = True
            self.continuous_move_right()

    def continuous_move_right(self):
        if self.moving_right:
            self.move_right()
            turtle.ontimer(self.continuous_move_right, 50)

    def stop_moving_right(self):
        self.moving_right = False
