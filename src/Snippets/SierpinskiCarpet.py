from turtle import Screen, Turtle


def sierpinski(level, turtle, length, direction=90):
    for _ in range(4):
        turtle.forward(length)
        turtle.left(direction)

    if level > 1:
        for _ in range(4):
            turtle.forward(length)
            turtle.left(direction)
            sierpinski(level - 1, turtle, int(length / 2), direction)


def main():
    length = 400
    n = 4
    screen = Screen()
    turtle = Turtle()
    turtle.speed('fastest')
    screen.title("Sierpinski triangle n=" + str(n))

    turtle.penup()
    turtle.goto(-int(length/2), -int(length/3)-85)
    turtle.pendown()

    sierpinski(n, turtle, length)

    turtle.hideturtle()
    screen.exitonclick()


if __name__ == '__main__':
    main()
