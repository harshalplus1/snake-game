from turtle import Turtle,Screen
sc=Screen()
UP=90
RIGHT=0
LEFT=180
DOWN=270
TPOS=[]
class Snake:
    def __init__(self):
        self.i=0
    def move(self):
        tbody[0].forward(10)
    def body(self):
        sc.tracer(0)
        tur=Turtle()
        TPOS.append(-20*self.i)
        tbody.append(tur)
        if(tbody[0]!=tur):
            tur.goto(400,0)
        tur.penup()
        tur.color("white")
        tur.shape("square")
        self.i=self.i+1
        sc.listen()



    def moveforward(self):
        if tbody[0].heading() != DOWN:
            tbody[0].setheading(UP)

    def movebackward(self):
        if tbody[0].heading() != UP:
            tbody[0].setheading(DOWN)

    def moveright(self):
        if tbody[0].heading() != LEFT:
            tbody[0].setheading(RIGHT)

    def moveleft(self):
        if tbody[0].heading() != RIGHT:
            tbody[0].setheading(LEFT)

tbody=[]