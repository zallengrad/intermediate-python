from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270 )
        self.hideturtle()
        self.update_score()

    def GameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVERR!!", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)


