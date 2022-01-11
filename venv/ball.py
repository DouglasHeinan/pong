from turtle import Turtle
import random

class Ball(Turtle):
    
    """This object controls the ball as it bounces around the screen"""
    def __init__(self):
        super().__init__()
        self.make_ball()
        start_x_y = (-10, 10)
        self.x_adjust = random.choice(start_x_y)
        self.y_adjust = random.choice(start_x_y)

    """Creates the ball when initialized"""
    def make_ball(self):
        self.penup()
        self.color('white')
        self.shape('circle')

    """
    This moves the ball by changing the 'go-to' coordinates. 
    The x and y adjust start at 10 when the object is initialized, 
    but change when the ball bounces off of a wall or paddle.
    """
    def move_ball(self):
        new_x = self.xcor() + self.x_adjust
        new_y = self.ycor() + self.y_adjust
        self.goto(new_x, new_y)

    """Reverses the y-axis momentum of the ball when it comes into contact with the floor or ceiling"""
    def wall_bounce(self):
        self.y_adjust *= -1

    """Reverses the x-axis momentum of the ball whenever it comes into contact with a paddle"""
    def paddle_bounce(self):
        self.x_adjust *= -1

    """After one player scores a point, this method resets the games state, so long as neither player has ten points"""
    def reset_ball(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        start_x_y = (-10, 10)
        self.x_adjust = random.choice(start_x_y)
        self.y_adjust = random.choice(start_x_y)

