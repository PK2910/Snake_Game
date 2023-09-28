from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
snake_1=Snake()
food=Food()
score_1=Score()
screen.listen()
screen.onkey(snake_1.up,'Up')
screen.onkey(snake_1.down,'Down')
screen.onkey(snake_1.left,'Left')
screen.onkey(snake_1.right,'Right')
is_race=True
while is_race:
    screen.update()
    time.sleep(0.1)
    snake_1.move()
    #Detecting if the snake collides with the food:
    if snake_1.head.distance(food)<=15:
        food.location()
        snake_1.extend()
        score_1.increase()
    #Detecting collision of the snake with the wall
    if snake_1.head.xcor()>280 or snake_1.head.xcor()<-280 or snake_1.head.ycor()>280 or snake_1.head.ycor()<-280:
        is_race=False
        score_1.over()
    #Detect collision with tail
    for segment in snake_1.segments[1:]:  # Starting  from the second segment to skipping the head of the snake
        if snake_1.head.distance(segment) < 20: 
            is_race = False
            score_1.over()
screen.exitonclick()