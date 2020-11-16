import turtle
from turtle import Turtle

t = Turtle()


def hexagon(t, length):
    for count in range(6):
        t.forward(length)
        t.left(60)


def radialHexagons(t, n, length):
    for count in range(n):
        hexagon(t, length)
        t.left(360 / n)


radialHexagons(t, 4, 50)

turtle.done()