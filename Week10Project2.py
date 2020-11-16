import turtle
from turtle import *        # I changed the import from what it was to all (*)
import random                   # I added random, in order to randomize the number used in RGB.
from random import randint      # As well as randint


def randomColor():                  # Created a new function name randomColor() to randomize RGB numbers.
    colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = [r, g, b]
    return rgb


def cCurve(t, x1, y1, x2, y2, level):
    def drawLine(x1, y1, x2, y2):
        """Draws a line segment between the endpoints."""
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)

    if level == 0:
        drawLine(x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) // 2
        ym = (x2 + y1 + y2 - x1) // 2
        cCurve(t, x1, y1, xm, ym, level - 1)
        cCurve(t, xm, ym, x2, y2, level - 1)


def main():
    level = int(input("Enter the level (0 or greater): "))
    t = Turtle()
    if level > 8:
        tracer(False)
    t.pencolor(randomColor())                              # I changed the pencolor from "blue" to the randomColor() function.
    t.speed(0)
    t.hideturtle()
    cCurve(t, 50, -50, 50, 50, level)
    if level > 8:
        update()


if __name__ == "__main__":
    main()

turtle.done()
