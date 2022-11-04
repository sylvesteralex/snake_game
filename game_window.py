from turtle import Turtle, Screen

WIDTH, HEIGHT, MARGIN = 800, 800, 100
GAME_ZONE_LEFT, GAME_ZONE_RIGHT = -(WIDTH/2), (WIDTH/2)
GAME_ZONE_TOP, GAME_ZONE_BOTTOM = (HEIGHT/2), -(HEIGHT/2)


window = Screen()
window.setup(WIDTH + MARGIN, HEIGHT + MARGIN)
window.bgcolor("black")
window.title("Snake game")
window.tracer(0)


class Gamearea(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")

    def draw_line(self, start_pos=tuple(), end_pos=tuple()):
        self.goto(start_pos)
        self.pendown()
        self.goto(end_pos)
        self.penup()

    def draw_game_area(self):
        self.draw_line((GAME_ZONE_LEFT, GAME_ZONE_BOTTOM), (GAME_ZONE_RIGHT, GAME_ZONE_BOTTOM))  # bottom
        self.draw_line((GAME_ZONE_LEFT, GAME_ZONE_TOP), (GAME_ZONE_LEFT, GAME_ZONE_BOTTOM))  # left
        self.draw_line((GAME_ZONE_RIGHT, GAME_ZONE_TOP), (GAME_ZONE_RIGHT, GAME_ZONE_BOTTOM))  # right
        self.draw_line((GAME_ZONE_LEFT, GAME_ZONE_TOP), (GAME_ZONE_RIGHT, GAME_ZONE_TOP))  # top
