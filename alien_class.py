from turtle import Turtle
from ship_class import Bullet

XPOS = [-150, -100, -50, 0, 50, 100, 150]

class AlienBuilder(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.aliens = []
        self.bullets = []
        self.dead_aliens = []

    def build_row(self, ypos):
        for i in range(7):
            new_alien = Alien(xpos=XPOS[i], ypos=ypos)
            self.aliens.append(new_alien)


class Alien(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.goto(xpos, ypos)
        self.setheading(180)
        self.bullets = []

    def move(self):
        self.forward(10)

    def switch_directions(self):
        current_heading = self.heading()
        self.setheading(current_heading + 180)

    def shoot(self):
        new_bullet = Bullet(xpos=self.xcor(), ypos=self.ycor())
        self.bullets.append(new_bullet)
        new_bullet.setheading(270)
        new_bullet.color("red")
