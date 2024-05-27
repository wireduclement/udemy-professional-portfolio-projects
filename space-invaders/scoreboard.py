from turtle import Turtle

FONT = ("Courier", 12, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("path/to/your/data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(-300, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}\nHighscore: {self.highscore}", align="left", font=(FONT))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("path/to/your/data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", align="center",  font=(FONT))