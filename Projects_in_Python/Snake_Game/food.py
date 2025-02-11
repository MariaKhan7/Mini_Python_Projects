import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.refresh()
        self.color("green")

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 265)
        self.goto(rand_x, rand_y)
