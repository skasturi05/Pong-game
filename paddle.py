from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_LENGTH = 1
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.width = PADDLE_WIDTH
        self.length = PADDLE_LENGTH

    def create_paddle(self, x_pos, y_pos):
        self.goto(x_pos, y_pos)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=self.width, stretch_len=self.length)
        self.color("white")

    def up(self):
        new_ycor = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_ycor)

    def down(self):
        new_ycor = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_ycor)
