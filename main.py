import random
from turtle import Screen
from Turt import Turt
from cars import Cars
from ScoreBoard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Turtle Road")
screen.setup(height=600, width=600)
screen.listen()
screen.tracer(0)

turt = Turt()
cars = Cars()
board = Scoreboard()
turt.create_turtle()
cars.createCar()

screen.onkeypress(turt.moveUp, "Up")
screen.onkeypress(turt.moveDown, "Down")
screen.update()

for _ in range(15):
    cars.move()
poo = 2
run = True
while run:
    time.sleep(0.1)
    screen.update()
    if random.randint(1, poo) == 1:
        cars.createCar()
        cars.createCar()
        cars.createCar()
        cars.createCar()


    cars.move()

    for seg_num in cars.segment:
        if seg_num.distance(turt) < 15:
            board.gameOver()
            run = False
        elif turt.ycor() > 260:
            board.updateLvl()
            turt.goHome()
            cars.spepUp()



