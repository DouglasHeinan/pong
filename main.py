from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

SCREEN = Screen()


def main():
    """
    This program runs a two player game of the Atari classic game Pong.
    """
    SCREEN.setup(width=800, height=600)
    SCREEN.bgcolor('black')
    SCREEN.title('PONG!')

    ball = Ball()
    score = Score()
    left_paddle = Paddle(-350)
    right_paddle = Paddle(350)

    """
    The left player controls their paddle with the 'a' and 'z' buttons.
    The right player controls their paddle with the 'up' and 'down' buttons.
    """
    SCREEN.listen()
    SCREEN.onkey(left_paddle.go_up, 'a')
    SCREEN.onkey(left_paddle.go_down, 'z')
    SCREEN.onkey(right_paddle.go_up, 'Up')
    SCREEN.onkey(right_paddle.go_down, 'Down')

    game_over = False
    l_score = 0
    r_score = 0
    wait = 0.04
    bounce = 0
    """
    The main program runs for as long as the ball doesn't hit a wall
    """
    while not game_over:
        while 380 > ball.xcor() > -380:
            time.sleep(wait)
            SCREEN.update()
            ball.move_ball()

            """If the ball hits the floor or ceiling, it bounces"""
            if ball.ycor() > 270 or ball.ycor() < -270:
                print('wall_bounce')
                ball.wall_bounce()
                ball.move_ball()

            """
            If the ball makes contact with one of the players' paddles, it bounces using a different method.
            Also, the speed increases.
            """
            # if ball.distance(left_paddle) < 15 or ball.distance(right_paddle) < 15:
            if ball.distance(right_paddle) <= 50 and ball.xcor() >= 330 or \
                    ball.distance(left_paddle) <= 50 and ball.xcor() <= -330:
                ball.paddle_bounce()
                bounce += 1
                if bounce % 3 == 0:
                    wait /= 2
                ball.move_ball()
                ball.move_ball()

        """
        If the ball makes contact with one of the two side walls, somebody gets a point and the game resets 
        until somebody scores ten points.
        """
        if ball.xcor() >= 380:
            score.update('left')
            l_score += 1
        else:
            score.update('right')
            r_score += 1
        if l_score == 10 or r_score == 10:
            game_over = True
        else:
            ball.reset_ball()
            wait = 0.04
            bounce = 0

    SCREEN.exitonclick()


if __name__ == '__main__':
    main()
