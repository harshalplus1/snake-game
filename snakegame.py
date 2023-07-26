from turtle import Screen, Turtle
import time
from Snakebody import Snake, tbody
from window import Window
from Food import Food
from scoreboard import Display
SIZE = 500

s = Snake()
t = Turtle()
t.hideturtle()
t.color("white")

sc = Screen()
sc.tracer(0)
d = Display()


def anycor(t, size):
    tur=t
    if tur.ycor()<=-(size/2)+10 or tur.xcor()>=(size/2)-10 or tur.ycor()>=(size/2)-10 or tur.xcor()<=-(size/2)+10:
        return True
    return False


f=Food()
w=Window(sc)
sc.listen()
x=True
s.body()
s.body()
s.body()
s.body()
sc.onkey(fun=s.moveforward,key='w')
sc.onkey(fun=s.movebackward, key='s')
sc.onkey(fun=s.moveright, key='d')
sc.onkey(fun=s.moveleft, key='a')
while(x):
    time.sleep(0.075)
    for l in range(len(tbody)-1,0,-1):
        itrx = tbody[l - 1].xcor()
        itry = tbody[l - 1].ycor()
        tbody[l].goto(itrx, itry)
    s.move()
    if tbody[0].distance(f)< 14:
        s.body()
        d.update()
        f.move()
    if anycor(tbody[0], SIZE):
        x=False
    for i in tbody[1:]:
        if tbody[0].distance(i)<5:
            x=False
    if x==False:
        t.write("G A M E  O V E R",True,"center",("Arial",19,"normal"))
    sc.update()



sc.exitonclick()