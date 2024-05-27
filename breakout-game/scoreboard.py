from turtle import Turtle

FONT = ("Courier", 10, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("C:/Users/wired/Desktop/udemy/end-projects/breakout-game/data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(-300, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   Highscore: {self.highscore}", align="left", font=(FONT))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("C:/Users/wired/Desktop/udemy/end-projects/breakout-game/data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align="center",  font=(FONT))

    def check_game_done(self):
            self.goto(0, 0)
            self.write(f"Good job! All bricks are broken.\n\nHighscore: {self.highscore}", align="center",  font=(FONT))