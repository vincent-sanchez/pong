from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
right_paddle = Paddle(x=350, y=0)
left_paddle = Paddle(x=-350,y=0)
ball = Ball()
screen.listen()
scoreboard = Scoreboard()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down,"Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        if ball.move_speed != 0:
            ball.move_speed -= .001
    #Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Right paddle miss
    elif ball.xcor() >= 400:
        ball.reset_ball()
        scoreboard.l_point()
    #Left paddle miss
    elif ball.xcor() <= -400:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()