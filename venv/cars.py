from turtle import Turtle
import random

ran = [-200,-180,-160,-140,-120,-100,-80,-60,-40,-20,0,20,40,60,80,100,120,140,160,180,200]
class Cars(Turtle):

    def __init__(self):

        self.segment = []
        self.x = 0
        self.speedx = 0
        self.speedy = 10
    def createCar(self):
        rand = random.randint(1, 2)
        if rand == 1:
            cr = Turtle("square")
            cr.penup()
            cr.color("white", "white")
            cr.shapesize(0.5, 1)
            cr.setheading(180)
            cr.setposition(300, random.choice(ran))
            self.segment.append(cr)
            self.x += 40

    def move(self):
        for seg_num in self.segment:
            seg_num.forward(random.randint(self.speedx, self.speedy))

    def spepUp(self):
        self.speedx += 5
        self.speedy += 5
        print(f"{self.speedx},,{self.speedy}")



