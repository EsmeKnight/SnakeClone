from turtle import Turtle, color

ALIGNMENT = "center"
FONT = "courier"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.write_score()

    # increases score when food eaten. called in main
    def add(self):
        self.clear()
        self.score += 1
        self.write_score()

    # called by add to write score
    def write_score(self):
        self.pencolor("white")
        self.penup()
        self.goto(0, 267)
        self.write(f"Score: {self.score}", False, ALIGNMENT, (FONT, 24, "normal"))

    # called by main if snake head collides with another snake turtle
    def gameover(self):
        self.pencolor("white")
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGNMENT, (FONT, 30, "normal"))
