from turtle import Turtle


class Paddle(Turtle):

    """This object is the paddle the player uses to bounce the ball back and forth with"""
    def __init__(self, side):
        super().__init__()
        self.make_paddle(side)

    """Creates the paddle when initialized"""
    def make_paddle(self, side):
        self.hideturtle()
        self.penup()
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(side, 0)
        self.showturtle()

    """
    This pair of methods execute the up and down movement of the paddle 
    when the appropriate key is depressed by each player
    """
    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
