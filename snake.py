from turtle import Turtle


SNAKE_BODY_XWIDTH, MOVE_DIST = 20, 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self):
        self.snake_body_parts = []
        self.snake_body_xwidth = SNAKE_BODY_XWIDTH
        self.create_snake()
        self.head = self.snake_body_parts[0]
        # self.head.color("white", "red")

    def create_snake(self):
        self.add_segment(3, True)

    def add_segment(self, num_of_segments=int(), initial=False):
        ''' Create given number of snake segments
            Arguments:
            :num_of_segments -- number of segments to create
            :initial -- set True if it is initial instance of snake
        '''
        for body_part in range(num_of_segments):
            snake_body = Turtle("square")
            snake_body.color("white", "white")
            snake_body.penup()
            if initial:
                self.head_x, self.head_y = 0, 0
            else:
                self.head_x, self.head_y = self.snake_body_parts[-1].xcor(), self.snake_body_parts[-1].ycor()
                # print(self.head_x, self.head_y)
            snake_body.goto((self.head_x-self.snake_body_xwidth), self.head_y)
            self.snake_body_xwidth += (self.snake_body_xwidth / (body_part + 1))
            self.snake_body_parts.append(snake_body)

    def extend(self):
        tail_x, tail_y = self.snake_body_parts[-1].xcor(), self.snake_body_parts[-1].ycor()
        # print(tail_x, tail_y)
        self.add_segment(1)
        self.snake_body_parts[-1].goto((tail_x - SNAKE_BODY_XWIDTH), tail_y)
        # self.snake_body_parts[-1].color("green")

    def move(self):
        for body_part in range(len(self.snake_body_parts)-1, 0, -1):
            new_x = self.snake_body_parts[body_part - 1].xcor()
            new_y = self.snake_body_parts[body_part - 1].ycor()
            # print(new_x, new_y)
            self.snake_body_parts[body_part].goto(new_x, new_y)
        self.head.fd(MOVE_DIST)

    # MOVEMENTS
    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            # self.move()  # == testing

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            # self.move()  # == testing

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            # self.move()  # == testing

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            # self.move()  # == testing
