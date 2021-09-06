from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

XCOR_PADDLE_LEFT = -350
XCOR_PADDLE_RIGHT = 350
YCOR_PADDLE = 0

screen = Screen()

# Create screen
screen.setup(width=800, height=600)
screen.bgcolor("black")
central_divider = []
screen.tracer(0)
game_is_on = True

# Create scoreboards
scoreboard_left = Scoreboard()
scoreboard_right = Scoreboard()
scoreboard_left.create_score(-180)
scoreboard_right.create_score(180)

# Create paddles
paddle_right = Paddle()
paddle_right.create_paddle(XCOR_PADDLE_RIGHT, 0)

paddle_left = Paddle()
paddle_left.create_paddle(XCOR_PADDLE_LEFT, 0)

# Move and control the RIGHT paddle
screen.listen()
screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")

# Move and control the left paddle
screen.listen()
screen.onkeypress(paddle_left.up, "w")
screen.onkeypress(paddle_left.down, "s")

# Create ball
ball = Ball()
ball.speed("fastest")
while game_is_on:

    time.sleep(ball.move_speed)
    for yaxis in range(-300, 300, 20):
        divider = Turtle(shape="square")
        divider.color("white")
        divider.penup()
        divider.goto(0, yaxis)
        divider.shapesize(stretch_len=0.1, stretch_wid=0.5)
        central_divider.append(divider)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        # Collision with top or bottom wall detected. Ball needs to bounce
        ball.bounce_y()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 320:
        ball.bounce_x_r_paddle()
        scoreboard_right.increase()
        scoreboard_right.update_score()

    if ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x_l_paddle()
        scoreboard_left.increase()
        scoreboard_left.update_score()

    # If the ball misses the right paddle, then:
    if ball.xcor() > 380:
        # Go to start position
        ball.reset_position()
        # Increase the score of the left side player
        scoreboard_left.increase()
        scoreboard_left.update_score()

    # If the ball misses the left paddle, then:
    if ball.xcor() < -380:
        # Go to start position
        ball.reset_position()
        # Increase the score of the right side player
        scoreboard_right.increase()
        scoreboard_right.update_score()

screen.exitonclick()
