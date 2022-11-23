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
    n = 10
    screen = Screen()
    turtle = Turtle()
    screen.title("Sierpinski triangle n=" + str(n))
    screen.delay(0)

    turtle.ht()
    turtle.speed('fastest')
    turtle.penup()
    turtle.goto(-int(length/2), -int(length/3)-85)
    turtle.pendown()

    if n > 10:
        screen.tracer(0, 0)
        screen.title("PLEASE WAIT")
        sierpinski(n, turtle, length)
        screen.update()
        screen.title("Sierpinski triangle n=" + str(n))
    if n <= 10:
        sierpinski(n, turtle, length)

    screen.exitonclick()


if __name__ == '__main__':
    main()
