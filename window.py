class Window:
    def __init__(self,s):
        s.title("Snake Game")
        s.bgcolor("black")
        s.setup(500,500)
    def exit(self,s):
        s.exitonclick()