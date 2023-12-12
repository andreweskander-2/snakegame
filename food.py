from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.shapesize(0.8,0.8)
        self.color("orange")
        self.penup()
        self.refresh_food()

    def refresh_food(self):
            random_cord = random.randint(-260, 260)
            self.setpos(random_cord, random_cord)