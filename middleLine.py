from turtle import Turtle


class MiddleLine:
    def __init__(self):
        self.DrawLine()

    def DrawLine(self):
        line = []
        new_segment = Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.shapesize(stretch_wid=1, stretch_len=0.2)
        new_segment.goto(0, 400)
        new_segment.forward(10)
        line.append(new_segment)
        for i in range(40):
            new_segment = Turtle()
            new_segment.color("white")
            new_segment.shape("square")
            new_segment.penup()
            new_segment.shapesize(stretch_wid=1, stretch_len=0.2)
            new_y = line[-1].ycor() - 30
            new_segment.goto(0, new_y)
            line.append(new_segment)
            new_segment.forward(10)
