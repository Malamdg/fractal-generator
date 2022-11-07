# ||===========================================================================||
# || Source https://www.useblackbox.io/search : how to do fractals with python ||
# ||===========================================================================||
from turtle import *


def fractal(level):
    global length, direction

    for _ in range(3):
        forward(length)

        if level > 1:
            length /= 2
            direction = - direction
            fractal(level - 1)
            direction = - direction
            length *= 2

        right(direction)

    forward(length)
    right(direction)


if __name__ == "__main__":
    length = 140
    direction = 90

    fractal(7)

    hideturtle()
    exitonclick()
