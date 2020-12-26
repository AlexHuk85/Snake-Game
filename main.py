from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()

score_board = ScoreBoard()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

screen.listen()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.add_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        score_board.game_over()

    for s in snake.snake_body[1:]:
        if snake.head.distance(s) < 10:
            game_is_on = False
            score_board.game_over()


screen.exitonclick()
