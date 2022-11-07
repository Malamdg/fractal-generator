# ||===========================================================================||
# || Source https://www.useblackbox.io/search : how to do fractals with python ||
# ||===========================================================================||

from turtle import Screen, Turtle


def fractal(level, turtle, length, direction=90):
    for _ in range(3):
        turtle.forward(length)

        if level > 1:
            fractal(level - 1, turtle, int(length / 2), -direction)

        turtle.right(direction)

    turtle.forward(length)
    turtle.right(direction)


def main():
    screen = Screen()
    turtle = Turtle()
    turtle.speed('fastest')  # because I have no patience

    fractal(8, turtle, 100, 90)

    turtle.hideturtle()
    screen.exitonclick()


if __name__ == '__main__':
    main()
