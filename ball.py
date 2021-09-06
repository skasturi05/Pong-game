from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x_r_paddle(self):
        self.x_move = -(abs(self.x_move))
        self.move_speed *= 0.9

    def bounce_x_l_paddle(self):
        self.x_move = (abs(self.x_move))
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x_r_paddle()
        self.move_speed = 0.1
