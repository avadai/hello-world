import turtle
from turtle import Turtle

t = Turtle()


def square(t, length):
    for count in range(4):
        t.forward(length)
        t.left(90)


square(t, 200)

turtle.done()