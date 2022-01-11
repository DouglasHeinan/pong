from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Ariel'

class Score(Turtle):
    
    """This object keeps track of the score and adjusts the scoreboard"""
    def __init__(self):
        super().__init__()
        self.make_score_board()
        
    """This creates the initial score board in the top center of the screen"""
    def make_score_board(self):
        self.penup()
        self.speed('fastest')
        self.hideturtle()
        self.color('white')
        self.score_l = 0
        self.score_r = 0
        self.goto(-100, 270)
        self.write(arg=f"Left Player: {self.score_l}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 270)
        self.write(arg=f"Right Player: {self.score_r}", move=False, align=ALIGNMENT, font=FONT)


    """Whenever somebody scores a point, this updates the scoreboard to reflect the current score"""
    def update(self, side):
        self.clear()
        if side == 'left':
            self.score_l += 1
            self.goto(-100, 270)
            self.write(arg=f"Left Player: {self.score_l}", move=False, align=ALIGNMENT, font=FONT)
            self.goto(100, 270)
            self.write(arg=f"Right Player: {self.score_r}", move=False, align=ALIGNMENT, font=FONT)

        else:
            self.score_r += 1
            self.goto(-100, 270)
            self.write(arg=f"Left Player: {self.score_l}", move=False, align=ALIGNMENT, font=FONT)
            self.goto(100, 270)
            self.write(arg=f"Right Player: {self.score_r}", move=False, align=ALIGNMENT, font=FONT)
        if self.score_l == 10 or self.score_r == 10:
            self.game_end()

    """If somebody reaches ten points, this method creates a 'Game Over' screen"""
    def game_end(self):
        winner = 'Left Player'
        if self.score_r == 10:
            winner = 'Right Player'
        self.goto(0, 50)
        self.write(arg='Game Over', move=False, align=ALIGNMENT, font=FONT)
        self.goto(0, -50)
        self.write(arg=f"{winner} wins!", move=False, align=ALIGNMENT, font=FONT)