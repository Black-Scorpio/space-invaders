# main.py

import turtle
from config import SCREEN_WIDTH, SCREEN_HEIGHT, COLLISION_DISTANCE, NUM_ALIENS
from player import Player
from bullet import Bullet
from alien import Alien

# Screen setup
win = turtle.Screen()
win.title("Alien Shooter")
win.bgcolor("black")
win.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
win.tracer(0)

# Create player
player = Player()

# Create bullet
bullet = Bullet()

# Create aliens
aliens = []

# Create 2 rows of 5 aliens each in a grid pattern
start_x = -300
start_y = 250
for row in range(2):
    for col in range(NUM_ALIENS // 2):
        alien = Alien(start_x + col * 70, start_y - row * 50)
        aliens.append(alien)

# Keyboard bindings
win.listen()
win.onkeypress(player.start_moving_left, "Left")
win.onkeyrelease(player.stop_moving_left, "Left")
win.onkeypress(player.start_moving_right, "Right")
win.onkeyrelease(player.stop_moving_right, "Right")
win.onkeypress(player.start_moving_left, "a")
win.onkeyrelease(player.stop_moving_left, "a")
win.onkeypress(player.start_moving_right, "d")
win.onkeyrelease(player.stop_moving_right, "d")
win.onkey(lambda: bullet.fire(player), "space")

# Collision detection function
def is_collision(t1, t2):
    distance = t1.distance(t2)
    return distance < COLLISION_DISTANCE

# Display message function
def display_message(message):
    msg = turtle.Turtle()
    msg.color("white")
    msg.penup()
    msg.hideturtle()
    msg.goto(0, 0)
    msg.write(message, align="center", font=("Courier", 36, "normal"))

# Main game loop
game_over = False

while not game_over:
    win.update()

    for alien in aliens[:]:
        alien.move(aliens)

        if is_collision(bullet, alien):
            bullet.hideturtle()
            bullet.state = "ready"
            bullet.goto(0, -400)
            alien.hideturtle()
            aliens.remove(alien)

        if is_collision(player, alien):
            player.hideturtle()
            alien.hideturtle()
            display_message("Game Over")
            game_over = True
            break

    bullet.move()

    if not aliens:
        display_message("You Win")
        game_over = True

win.mainloop()
