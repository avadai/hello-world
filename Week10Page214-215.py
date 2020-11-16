import turtle
from turtle import Turtle
import random

t = Turtle()
t.screen.bgcolor("orange")
x = t.screen.window_width() // 2
y = t.screen.window_height() // 2
print((-x, y), (x, -y))


def randomWalk(t, turns, distance=20):
    for x in range(turns):
        if x % 2 == 0:
            t.left(random.randint(0, 270))
        else:
            t.right(random.randint(0, 270))
            t.forward(distance)


def main():
    t.shape("turtle")
    randomWalk(t, 40, 30)


if __name__ == "__main__":
    main()

turtle.done()