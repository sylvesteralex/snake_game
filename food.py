from turtle import Turtle
from random import randint
from game_window import WIDTH, HEIGHT, GAME_ZONE_LEFT, GAME_ZONE_RIGHT, GAME_ZONE_TOP, GAME_ZONE_BOTTOM


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("white", "white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        pos_x = randint(int(GAME_ZONE_LEFT + (WIDTH/20)), int(GAME_ZONE_RIGHT - (WIDTH/20)))
        pos_y = randint(int(GAME_ZONE_BOTTOM + (HEIGHT/20)), int(GAME_ZONE_TOP - (HEIGHT/20)))
        self.goto(pos_x, pos_y)


class SlowFood(Food):
    def __init__(self):
        super().__init__()
        self.color("blue", "blue")

class SpeedFood(Food):
    def __init__(self):
        super().__init__()
        self.color("red", "red")

