import turtle
from turtle import Turtle


def square(t, length):
    for count in range(4):
        t.forward(length)
        t.left(90)


def hexagon(t, length):
    for count in range(6):
        t.forward(length)
        t.left(60)


def radialpattern(t, n, length, shape):
    for count in range(n):
        shape(t, length)
        t.left(360 / n)


t = Turtle()
radialpattern(t, n=10, length=50, shape=square)
t.clear()
radialpattern(t, n=10, length=50, shape=hexagon)


turtle.done()