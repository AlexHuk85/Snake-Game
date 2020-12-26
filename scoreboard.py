from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 15, "normal")
COLOR = 'white'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color(COLOR)
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align=ALIGNMENT, font=FONT)
