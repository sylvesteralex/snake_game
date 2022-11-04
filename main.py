from game_window import window, Gamearea, GAME_ZONE_LEFT, GAME_ZONE_RIGHT, GAME_ZONE_TOP, GAME_ZONE_BOTTOM
from time import sleep
from snake import Snake
from food import Food, SlowFood, SpeedFood
from scoreboard import Scoreboard, Infoboard
from intro import intro


def init():
    intro()
    new_game()


def new_game():
    window.resetscreen()
    snake_game()


def snake_game():
    gamearea = Gamearea()
    gamearea.draw_game_area()

    snake = Snake()

    scoreboard = Scoreboard()
    scoreboard.read_score_list()
    infoboard = Infoboard()

    food = Food()
    slow_food = SlowFood()
    speed_food = SpeedFood()

    window.update()
    # print(snake_body_parts)

    window.onkey(snake.go_up, "w")
    window.onkey(snake.go_up, "Up")
    window.onkey(snake.go_down, "s")
    window.onkey(snake.go_down, "Down")
    window.onkey(snake.go_left, "a")
    window.onkey(snake.go_left, "Left")
    window.onkey(snake.go_right, "d")
    window.onkey(snake.go_right, "Right")
    window.onkey(new_game, "r")
    window.listen()

    game_is_on = True
    time_slow_turn_is_on = False
    time_fast_turn_is_on = False
    # time_speed_turn = 0
    while game_is_on:
        # # time speed with turns
        # if time_slow_turn_is_on:
        #     time_speed_turn += 1
        #     if time_slow_turn_is_on and time_speed_turn < 15:
        #         time_speed = 0.4
        #     else:
        #         time_speed = 0.1
        #         time_slow_turn_is_on = False
        #         time_speed_turn = 0
        #         slow_food.refresh()

        if time_slow_turn_is_on:
            time_speed = 0.4
        elif time_fast_turn_is_on:
            time_speed = 0.05
        else:
            time_speed = 0.1

        window.update()
        sleep(time_speed)
        snake.move()

        # detect collision -- regular food
        if snake.head.distance(food) < 15:
            print("nom, nom")
            time_fast_turn_is_on = False
            time_slow_turn_is_on = False
            snake.head.color("white", "white")
            food.refresh()
            scoreboard.add_point()
            snake.extend()

        # detect collision -- slow time food
        if snake.head.distance(slow_food) < 15:
            print("slooow dooown....")
            time_fast_turn_is_on = False
            time_slow_turn_is_on = True
            snake.head.color("blue", "blue")
            slow_food.refresh()
            # scoreboard.add_point()
            # snake.extend()

        # detect collision -- speed time food
        if snake.head.distance(speed_food) < 15:
            print("getting faster!!!!")
            time_slow_turn_is_on = False
            time_fast_turn_is_on = True
            snake.head.color("red", "red")
            speed_food.refresh()
            # scoreboard.add_point()
            # snake.extend()

        # detect collision with walls
        if snake.head.xcor() > GAME_ZONE_RIGHT or snake.head.xcor() < GAME_ZONE_LEFT:
            scoreboard.new_high_score()
            game_is_on = False
        if snake.head.ycor() > GAME_ZONE_TOP or snake.head.ycor() < GAME_ZONE_BOTTOM:
            scoreboard.new_high_score()
            game_is_on = False

        # detect collision with itself
        for segment in snake.snake_body_parts[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.new_high_score()
                game_is_on = False

    window.exitonclick()


if __name__ == '__main__':
    init()
