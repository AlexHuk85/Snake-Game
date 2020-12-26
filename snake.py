from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_leght = 3
        self.snake_body = []
        self.starting_x = 0
        self.starting_y = 0

        for i in range(self.snake_leght):
            self.add_body()

        self.head = self.snake_body[0]

    def move(self):
        for snake in range(len(self.snake_body) - 1, 0, - 1):
            new_x = self.snake_body[snake - 1].xcor()
            new_y = self.snake_body[snake - 1].ycor()
            self.snake_body[snake].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_body()

    def add_body(self):
        snake = Turtle(shape='square')
        snake.penup()
        snake.color('white')
        snake.goto(self.starting_x, self.starting_y)
        self.starting_x -= 20
        self.snake_body.append(snake)
