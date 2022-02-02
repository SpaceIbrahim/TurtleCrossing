from turtle import Turtle

class Turt(Turtle):

    def __int__(self):
        super().__init__()
        

    def create_turtle(self):
        self.shape("turtle")
        self.penup()
        self.color("white", "white")
        self.goto(x= 0, y= -280)
        self.setheading(90)
        
    def moveUp(self):
        self.forward(20)

    def moveDown(self):
        self.backward(20)

    def goHome(self):
        self.setposition(x=0, y=-280)
        
