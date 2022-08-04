from random import randint
from turtle import Turtle


from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.move()

    def move(self):
        rand_x = randint(-290, 290)
        rand_y = randint(-290, 290)
        self.goto(rand_x, rand_y)
