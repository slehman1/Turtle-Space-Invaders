'''Space Invaders'''
#use turtle for gui
#ship class which moves left and rght and has a shoot bullet method
#enemies class which moves left and right and also has a shoot bullet method
#will have 3 lives and a while loop that continues until lives out
import time
import random
from turtle import *
from ship_class import Ship
from alien_class import AlienBuilder
from score_class import Scoreboard

lives = 3
score = 0

screen = Screen()
screen.addshape("new_spaceship.gif")
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)
screen.listen()

my_scoreboard = Scoreboard()
my_ship = Ship("new_spaceship.gif")
my_alien_builder = AlienBuilder()
my_alien_builder.build_row(ypos=200)
my_alien_builder.build_row(ypos=150)
my_alien_builder.build_row(ypos=100)


screen.onkey(my_ship.move_left, "Left")
screen.onkey(my_ship.move_right, "Right")
screen.onkey(my_ship.shoot, "space")

count = 0
while lives > 0:
    count += 1
    screen.update()
    #shoot three bullet from each row every 10 counts
    if count % 10 == 0:
        if my_alien_builder.aliens:
            for i in range(2):
                shooter = random.choice(my_alien_builder.aliens)
                shooter.shoot()
        else:
            my_scoreboard.win(score)

    #aliens move sideways
    for alien in my_alien_builder.aliens:
        alien.move()

    #alien coming towards edge
    for alien in my_alien_builder.aliens:
        if alien.xcor() > 280 or alien.xcor() < -280:
            for alien in my_alien_builder.aliens:
                alien.switch_directions()

    #moving ship bullets forward
    for bullet in my_ship.bullets:
        bullet.move_forward()

    #moving alien bullets forward
    for alien in my_alien_builder.aliens:
        for bullet in alien.bullets:
            bullet.move_forward()
    for alien in my_alien_builder.dead_aliens:
        for bullet in alien.bullets:
            bullet.move_forward()

    #losing lives
    for alien in my_alien_builder.aliens:
        for bullet in alien.bullets:
            if bullet.distance(my_ship) < 20:
                alien.bullets.remove(bullet)
                bullet.hideturtle()
                lives -= 1
                my_scoreboard.update_scoreboard(score, lives)
                if alien.bullets:
                    for bullet in alien.bullets:
                        bullet.hideturtle()

    #shooting down aliens
    for alien in my_alien_builder.aliens:
        for bullet in my_ship.bullets:
            if bullet.distance(alien) < 20:
                alien.hideturtle()
                my_ship.bullets.remove(bullet)
                bullet.hideturtle()
                score += 20
                my_scoreboard.update_scoreboard(score, lives)
                my_alien_builder.dead_aliens.append(alien)
                my_alien_builder.aliens.remove(alien)
                for alien in my_alien_builder.dead_aliens:
                    for bullet in alien.bullets:
                        bullet.hideturtle()


    time.sleep(0.1)

my_scoreboard.game_over(score=score)

screen.exitonclick()