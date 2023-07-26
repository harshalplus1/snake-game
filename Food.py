from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.goto(random.randint(-229,229),random.randint(-229,229))
        self.shape("circle")
        self.color("blue")
    def move(self):
        self.goto(random.randint(-229, 229), random.randint(-229, 229))