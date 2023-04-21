from turtle import Turtle


class Paddle:
    def __init__(self):
        self.paddle = []
        self.create_paddle()
        self.starting_pos()

    def create_paddle(self):
        for i in range(2):
            new_paddle = Turtle()
            new_paddle.shape("square")
            new_paddle.color("white")
            new_paddle.shapesize(stretch_wid=5, stretch_len=1)
            self.paddle.append(new_paddle)

    def starting_pos(self):
        self.paddle[0].penup()
        self.paddle[1].penup()
        self.paddle[0].goto(-465, 0)
        self.paddle[1].goto(460, 0)

    def move_up(self):
        new_y = self.paddle[0].ycor() + 40
        self.paddle[0].goto(self.paddle[0].xcor(), new_y)

    def move_down(self):
        new_y = self.paddle[0].ycor() - 40
        self.paddle[0].goto(self.paddle[0].xcor(), new_y)

    def move_up_2(self):
        new_y = self.paddle[1].ycor() + 40
        self.paddle[1].goto(self.paddle[1].xcor(), new_y)

    def move_down_2(self):
        new_y = self.paddle[1].ycor() - 40
        self.paddle[1].goto(self.paddle[1].xcor(), new_y)
