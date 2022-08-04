from turtle import Turtle, color

ALIGNMENT = "center"
FONT = "courier"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_score()

    def add(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, ALIGNMENT, (FONT, 24, "normal"))

    def gameover(self):
        self.pencolor("white")
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGNMENT, (FONT, 30, "normal"))
