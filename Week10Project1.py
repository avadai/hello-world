import turtle
import math         # <- Math module for using pi to calculate the distance

t = turtle.Turtle()


def drawCircle(center, radius):                # <- drawCircle with set centerpoint (of 0 after it)
    degree = 3                                  # <- Degree of how much the turtle turns to make the circle
    count = 0
    center = (2.0 * math.pi * radius / 120)        # <- Calculating the distance moved
    t.home()
    t.setheading(degree)
    while count <= 120:                         # <- While statement that moves the turtle forward until it returns to the start
        t.down()
        t.forward(2.0 * math.pi * radius / 120)
        t.up()
        degree += 3
        t.setheading(degree)
        count += 1


drawCircle(0.0, 100)       # <- Centerpoint set for 0.0 and the radius of the circle is 100


turtle.done()       # <- Keeps the turtle graphic open until we close it