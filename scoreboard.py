from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def create_score(self, x_cord):
        self.goto(x_cord, 180)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write(arg=str(self.score), move=False, align="center", font=("Courier", 48, "bold"))

    def increase(self):
        self.score += 1
        return self.score

    def update_score(self):
        self.clear()
        self.penup()
        self.write(arg=str(self.score), move=False, align="center", font=("Courier", 48, "bold"))
