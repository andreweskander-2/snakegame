from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.write(arg=f"Your Score is: {self.score}      High Score: {self.high_score}", align='center', font=('Arial', 14, 'normal'))


    def update_score(self):
        self.score +=1
        self.clear()
        self.write(arg=f"Your Score is: {self.score}      High Score: {self.high_score}", align='center', font=('Arial', 14, 'normal'))


    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write(arg=f"Your Score is: {self.score}      High Score: {self.high_score}", align='center', font=('Arial', 14, 'normal'))
