from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 12
        self.y_move = 12
        self.hit_count = 0

    def move(self):
        x = self.xcor() - self.x_move
        y = self.ycor() - self.y_move
        self.goto(x, y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.x_bounce()
        self.hit_count = 0

    def increase_speed(self):
        self.hit_count += 1
        if self.hit_count % 9 == 0:
            self.x_move *= 1.5
            self.y_move *= 1.5
            self.hit_count = 0

    def is_at_top(self):
        return self.ycor() > 275

    def is_at_side(self):
        return self.xcor() > 370 or self.xcor() < -370

    def out_of_bounds(self):
        return self.ycor() < -280
    
