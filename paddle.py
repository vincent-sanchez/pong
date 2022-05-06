from turtle import Turtle

MOVE_DISTANCE = 10
X_BOUNDARY = 230
Y_BOUNDARY = 220

class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.setx(x)
        self.sety(y)
        self.speed(9)
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.showturtle()

    def up(self):
        if self.ycor() <= X_BOUNDARY:
            self.goto(self.xcor(), (self.ycor()+MOVE_DISTANCE))
        else:
            pass

    def down(self):
        if self.ycor() >= -Y_BOUNDARY:
            self.goto(self.xcor(),(self.ycor()-MOVE_DISTANCE))
        else:
            pass

