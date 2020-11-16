import turtle

t = turtle.Turtle()


def drawSquare(t, x, y, length):
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)


drawSquare(t, 90, 90, 200)

turtle.done()