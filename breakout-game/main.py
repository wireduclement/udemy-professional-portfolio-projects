from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard
import time

def clear_screen():
    screen.clear()
    screen.bgcolor("black")

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Breakout Game Designed by Clement Wiredu")
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle((0, -275))
bricks = Brick((1000, 1000))
ball = Ball()
scoreboard = Scoreboard()

brick_list = []
x, y = 335, 250

for row in range(4):
    for col in range(9):
        brick_list.append(Brick((x, y)))
        x -= 85
    x = 335
    y -= 25


screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    scoreboard.update_score()

    # detect when the ball hits the upper wall
    if ball.is_at_top():
        ball.y_bounce()

    # detect when the ball hits both the side of the walls
    if ball.is_at_side():
        ball.x_bounce()

    # detect when the ball hits paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -245:
        ball.y_bounce()

    # detect when the ball hits the lower wall
    if ball.out_of_bounds():
        game_on = False
        scoreboard.reset()
        scoreboard.game_over()

    # detect when the ball hits bricks
    for brick in brick_list:
        if ball.distance(brick) < 23:
            brick.goto(1000, 1000)
            ball.y_bounce()
            brick_list.remove(brick)
            scoreboard.score += 1
            scoreboard.update_score()
            ball.increase_speed() 

    # check if the last brick is broken and update the score on the screen
    if len(brick_list) == 0:
        scoreboard.update_score()
        scoreboard.reset()
        clear_screen()  
        scoreboard.check_game_done()
        game_on = False


screen.exitonclick()