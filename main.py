import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

# calls movement functions from snake.py on keypress
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        food.move()
        snake.extend()
        scoreboard.add()
    if snake.head.xcor() >= 300:
        snake.right_collision()
    if snake.head.xcor() <= -300:
        snake.left_collision()
    if snake.head.ycor() >= 300:
        snake.top_collision()
    if snake.head.ycor() <= -300:
        snake.bottom_collision()

    # detect collision with self (except head)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()

    snake.move()


screen.exitonclick()
