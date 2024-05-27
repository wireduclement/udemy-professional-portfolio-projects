from turtle import Turtle, Screen
import random
import scoreboard

screen = Screen()

LEFT = -680 / 2   # window frame width
RIGHT = 680 / 2
TOP = 700 / 2     # window frame height
BOTTOM = -610 / 2 
ALIEN_SPEED = 0.3
ALIEN_SPAWN_INTERVAL = 1.5
FLOOR_LEVEL = 1 * BOTTOM


class Invaders(Turtle):

    def __init__(self):
        super().__init__()
        self.aliens = []
        self.alien_speed = ALIEN_SPEED
        self.alien_timer = 0
        self.kill_alien_count = 0

    def create_alien(self):
        new_alien = Turtle("turtle")
        new_alien.turtlesize(1.5)
        new_alien.color("white")
        new_alien.penup()
        new_alien.setposition(random.randint(int(LEFT), int(RIGHT)), TOP)
        new_alien.setheading(270)
        self.aliens.append(new_alien)

    def move_aliens(self):
        for alien in self.aliens:
            alien.forward(self.alien_speed)
            # Remove alien if it goes off the screen
            if alien.ycor() < BOTTOM:
                alien.hideturtle()
                self.aliens.remove(alien) 

    def check_collision(self, laser):
        for alien in self.aliens:
            if laser.distance(alien) < 20:
                return alien
        return None

    def hit_bottom(self):
        for alien in self.aliens:
            alien.forward(ALIEN_SPEED)
            if alien.ycor() < FLOOR_LEVEL:
                return True
