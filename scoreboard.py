from turtle import Turtle

class Display(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.newscore()

    def newscore(self):
        self.goto(0,230)
        self.write(f"Score = {self.score}", True, align="center",font=("Arial",8,"normal"))

    def update(self):
        self.score=self.score+1
        self.clear()
        self.newscore()