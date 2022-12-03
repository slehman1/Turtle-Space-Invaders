from turtle import Turtle
import time

class Ship(Turtle):
    def __init__(self, shape):
        super().__init__()
        self.shape(shape)
        self.color("green")
        self.penup()
        self.goto(0, -200)
        self.bullets = []
        self.last_shot = int(time.time())


    def move_right(self):
        self.forward(10)

    def move_left(self):
        self.back(10)

    def shoot(self):
        if int(time.time()) > self.last_shot + 1:
            x_cord = self.xcor()
            y_cord = self.ycor()
            new_bullet =Bullet(xpos=x_cord, ypos=y_cord)
            self.bullets.append(new_bullet)
            self.last_shot = int(time.time())


class Bullet(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.penup()
        self.setheading(90)
        self.goto(xpos, ypos)

    def move_forward(self):
        self.forward(10)
