from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from middleLine import MiddleLine
import time
import random

lst = [(154, 80, 38), (207, 159, 105), (181, 175, 18), (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105),
       (13, 37, 97), (72, 43, 23), (50, 121, 23), (187, 133, 150), (94, 192, 47),
       (106, 32, 54), (195, 94, 75), (25, 97, 25), (100, 120, 169), (180, 206, 170), (250, 169, 173), (24, 53, 110),
       (251, 171, 163), (149, 191, 244), (104, 60, 18), (81, 30, 46), (132, 79, 90), (18, 75, 105)]


def random_color():
    color = random.choice(lst)
    return color


screen = Screen()
screen.bgcolor("black")
screen.screensize(600, 800)
screen.tracer(0)

racket = Paddle()
ball = Ball()
scoreboard_1 = Scoreboard()
halfLine = MiddleLine()

screen.colormode(255)
screen.listen()
screen.onkey(racket.move_up, "w")
screen.onkey(racket.move_down, "s")
screen.onkey(racket.move_up_2, "Up")
screen.onkey(racket.move_down_2, "Down")

is_game_on = True
halfLine.DrawLine()
while is_game_on:
    time.sleep(0.03)
    screen.update()
    ball.movement()
    if ball.ycor() > 400 or ball.ycor() < -400:
        ball.bounce_upper()

    elif ball.xcor() > racket.paddle[1].xcor() - 20 and ball.distance(racket.paddle[1]) < 50:
        ball.bounce_right()
        new_color = random_color()
        ball.color(new_color)
        racket.paddle[1].color(new_color)
        scoreboard_1.update_r_score()
    elif ball.xcor() < racket.paddle[0].xcor() + 20 and ball.distance(racket.paddle[0]) < 50:
        ball.bounce_left()
        new_color_2 = random_color()
        ball.color(new_color_2)
        racket.paddle[0].color(new_color_2)
        scoreboard_1.update_l_score()

    elif ball.xcor() >= 465 and ball.distance(racket.paddle[0]) > 50:
        is_game_on = False
        scoreboard_1.gameOver()

    elif ball.xcor() <= -473 and ball.distance(racket.paddle[1]) > 50:
        is_game_on = False
        scoreboard_1.gameOver()


screen.exitonclick()
