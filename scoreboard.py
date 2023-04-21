from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.speed("fastest")
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-120, 350)
        self.write(self.l_score, font=("Arial", 30, "normal"))
        self.goto(120, 350)
        self.write(self.r_score, font=("Arial", 30, "normal"))

    def update_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def update_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def gameOver(self):
        self.goto(6, 0)
        self.write("GAME OVER", align="center",
                   font=("Arial", 30, "normal"))

