from turtle import Screen, Turtle


def sierpinski(level, turtle, length):
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)

    if level > 1:
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
            sierpinski(level - 1, turtle, int(length / 2))


def main():
    length = 900
    n = 9
    screen = Screen()
    turtle = Turtle()
    screen.title("Sierpinski triangle n=" + str(n))
    screen.delay(0)

    turtle.ht()
    turtle.speed('fastest')
    turtle.penup()
    turtle.goto(-int(length/2), -int(length/3)-85)
    turtle.pendown()

    sierpinski(n, turtle, length)

    turtle.hideturtle()
    screen.exitonclick()


if __name__ == '__main__':
    main()
