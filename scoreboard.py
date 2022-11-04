from turtle import Turtle
from game_window import HEIGHT, WIDTH, MARGIN


ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')
SMALL_FONT = ('Courier', 12, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.highest_points = 0
        self.hideturtle()
        self.goto(0, (((HEIGHT + MARGIN)/2) - (HEIGHT/20)))
        self.penup()
        self.pencolor("white")
        self.update_scoreboard()

    def new_high_score(self):
        if self.points > int(self.highest_points):
            self.highest_points = self.points
            self.update_scoreboard()
            self.update_score_list()
        self.game_over()

    def update_score_list(self):
        with open("score_list.txt", "r+") as f:
            previous_scores = f.read()
            f.seek(0)
            f.write(str(self.highest_points) + "\n" + previous_scores)

    def read_score_list(self):
        with open("score_list.txt", "r") as f:
            latest_high_score = f.readline()
            self.highest_points = int(latest_high_score)
            self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.points} | Highest score: {self.highest_points}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.points += 1
        self.update_scoreboard()


class Infoboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, (((HEIGHT + MARGIN)/2) - (HEIGHT/20)))
        self.penup()
        self.pencolor("white")
        self.keys_info()

    def keys_info(self):
        self.goto((-(WIDTH/2) + 2*(WIDTH/20)), (((HEIGHT + MARGIN)/2) - (HEIGHT/20)))
        self.write("R - restart", align=ALIGNMENT, font=SMALL_FONT)
