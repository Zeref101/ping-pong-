from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.color("blue")
        self.shape("circle")
        self.speed("fast")
        self.penup()
        self.move_x = 10
        self.move_y = 10

    def movement(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_upper(self):
        self.move_y *= -1
        new_y = self.ycor() + self.move_y
        self.goto(self.xcor(), new_y)

    def bounce_right(self):
        self.move_x *= -1
        self.move_y *= 1
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_left(self):
        self.move_x *= -1
        self.move_y *= 1
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

