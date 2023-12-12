import time
from turtle import Turtle, Screen

MOVING_DIS = 20
INIT_POS = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in INIT_POS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.setpos(position)
        self.body.append(new_segment)

    def elongate(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            new_pos = self.body[segment - 1].pos()
            self.body[segment].goto(new_pos)
        self.body[0].forward(MOVING_DIS)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.body[0].seth(0)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.body[0].seth(180)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.body[0].seth(90)

    def turn_down(self):
        if self.head.heading() != UP:
            self.body[0].seth(270)

    def turnings(self):
        screen = Screen()
        screen.onkey(key="Up", fun=self.turn_up)
        screen.onkey(key="Down", fun=self.turn_down)
        screen.onkey(key="Right", fun=self.turn_right)
        screen.onkey(key="Left", fun=self.turn_left)


    def refresh_pos(self):
        for seg in self.body:
            seg.goto(1000,1000)
        self.body = []
        self.create_snake()
        self.head = self.body[0]
