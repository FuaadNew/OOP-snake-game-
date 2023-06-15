from turtle import Turtle, Screen
import time
from Snake import snake
from food import Food
from scoreboard import Scoreboard
square1 = Turtle()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = snake()
food = Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor()< -280:
        scoreboard.reset()
        snake.reset()
    for segment in snake.segment_list[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()