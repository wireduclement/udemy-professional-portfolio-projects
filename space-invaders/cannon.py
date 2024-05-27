from turtle import Turtle

LEFT = -900 / 2   # window width
RIGHT = 900 / 2
TOP = 700 / 2   # window height
BOTTOM = -700 / 2 
FLOOR_LEVEL = 0.9 * BOTTOM
CANNON_MOVE = 10
LASER_LENGTH = 20
LASER_SPEED = 5

class LaserCannon(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(1, 1, 1)
        self.shape("square")
        self.setposition(0, FLOOR_LEVEL)
        self.lasers = []

    def draw_cannon(self):
        self.clear()
        self.turtlesize(1, 4)
        self.stamp()
        self.sety(FLOOR_LEVEL + 10)
        self.turtlesize(1, 1.5)  # Next tier
        self.stamp()
        self.sety(FLOOR_LEVEL + 20)
        self.turtlesize(0.8, 0.3)  # Tip of cannon
        self.stamp()
        self.sety(FLOOR_LEVEL)

    def go_left(self):
        x = self.xcor()
        if x > -380:
            self.setx(x - CANNON_MOVE)
            self.draw_cannon()

    def go_right(self):
        x = self.xcor()
        if x < 380:
            self.setx(x + CANNON_MOVE)
            self.draw_cannon()

    def shoot(self):
        new_laser = Turtle()
        new_laser.shape("square")
        new_laser.color("red")
        new_laser.shapesize(stretch_wid=0.2, stretch_len=1)
        new_laser.penup()
        new_laser.setposition(self.xcor(), self.ycor() + 20)
        new_laser.setheading(90)
        self.lasers.append(new_laser)

    def move_laser(self):
        for laser in self.lasers:
            laser.forward(LASER_SPEED)
            # Remove laser if it goes off the screen
            if laser.ycor() > TOP:
                laser.clear()
                laser.hideturtle()
                self.lasers.remove(laser)