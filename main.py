from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

#Define Objects from Classes
score = Score()
food = Food()
screen = Screen()
snake_1 = Snake()

#Define screen variables required for the game setup
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)                       #Helps with animating the snake movement smoothly
screen.listen()                        #Listens for keystrokes

#The screen limit the snake can reach without Game Over!
UPPER_LIMIT = 290
LOWER_LIMIT = -290

#Starting the game
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake_1.move()
    snake_1.turnings()

    # Determine the Snake-Food collision rule
    if snake_1.head.distance(food) < 15:
        food.refresh_food()
        snake_1.elongate()
        score.update_score()

    # Determine the Snake-Wall collision rule
    if snake_1.head.xcor() > UPPER_LIMIT or snake_1.head.xcor() < LOWER_LIMIT or snake_1.head.ycor() > UPPER_LIMIT or snake_1.head.ycor() < LOWER_LIMIT:
        score.game_over()
        snake_1.refresh_pos()

    # Determine the Snake-Snake_Body collision rule
    for snake_segment in snake_1.body[1:]:
        if snake_1.head.distance(snake_segment.pos()) < 10:
            score.game_over()
            snake_1.refresh_pos()





screen.exitonclick()
