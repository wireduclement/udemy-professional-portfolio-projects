from turtle import Screen, Turtle
from cannon import LaserCannon
from invaders import Invaders, ALIEN_SPAWN_INTERVAL
from scoreboard import Scoreboard
import time

game_running = False
FONT = ("Courier", 12, "bold")

def show_start_message(screen):
    message_turtle = Turtle()
    message_turtle.color("white")
    message_turtle.hideturtle()
    message_turtle.penup()
    message_turtle.goto(0, 0)
    message_turtle.write( "Instructions:\n1. Use Left/Right arrow keys to move\n2. Press Space to shoot\n\nPress 's' to start the game", align="center", font=FONT)
    message_turtle.goto(-100, -200)
    message_turtle.write("Designed By Wiredu Clement ®")


    def start_game():
        global game_running
        message_turtle.clear()
        screen.onkeypress(None, 's')  # Unbind 's' key
        game_running = True

    screen.onkeypress(start_game, 's')
    screen.listen()

def setup_game():
    global game_running

    screen = Screen()
    screen.setup(width=900, height=700)
    screen.title("Space Invaders")
    screen.bgpic("C:/Users/wired/Desktop/udemy/end-projects/space-invaders/space.png")
    screen.tracer(0)

    show_start_message(screen)

    # Wait until the 's' key is pressed to start the game
    while not game_running:
        screen.update()

    cannon = LaserCannon()
    invaders = Invaders() 
    scoreboard = Scoreboard() 

    screen.listen()
    screen.onkeypress(cannon.go_left, "Left")
    screen.onkeypress(cannon.go_right, "Right")
    screen.onkeypress(cannon.shoot, "space")

    alien_timer = 0
    
    while game_running:
        if time.time() - alien_timer > ALIEN_SPAWN_INTERVAL:
            invaders.create_alien()
            alien_timer = time.time()
        invaders.move_aliens()
        cannon.move_laser()
        screen.update()
        cannon.draw_cannon()
        scoreboard.update_score()

        # detect if laser hit alien
        if invaders.aliens:
            for laser in cannon.lasers:
                hit_alien = invaders.check_collision(laser)
                if hit_alien:
                    hit_alien.hideturtle()
                    laser.hideturtle()
                    invaders.aliens.remove(hit_alien)
                    cannon.lasers.remove(laser)
                    scoreboard.score += 1
                    scoreboard.update_score()
        screen.update()

        # detect if alien hits the bottom
        if invaders.hit_bottom():
            game_running = False
            scoreboard.reset()
            scoreboard.game_over()
            break
        screen.update()

    screen.exitonclick()

setup_game()
