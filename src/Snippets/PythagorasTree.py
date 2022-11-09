from turtle import *
from math import *
from random import uniform


def square(length, turtle):
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)


def coloredSquare(turtle, length):
    turtle.fillcolor(uniform(0, 1), uniform(0, 1), uniform(0, 1))
    turtle.begin_fill()
    square(length, turtle)
    turtle.end_fill()


def pythagorasTree(turtle, level, max_level, length):
    # Break condition
    if level == 0:
        return

    # ||======||
    # || KNOT ||
    # ||======||
    square(length, turtle)
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()

    # ||================||
    # || BRANCH DRAWING ||
    # ||================||
    branch_length = int(length / sqrt(2))

    # Left branch
    turtle.left(45)
    pythagorasTree(turtle, level - 1, max_level, branch_length)

    # Right branch
    turtle.right(90)
    turtle.penup()
    turtle.forward(branch_length)
    turtle.pendown()
    pythagorasTree(turtle, level - 1, max_level, branch_length)
    turtle.penup()
    turtle.back(branch_length)
    turtle.pendown()

    # Return to correct point and angle to have correct recursion
    turtle.left(45)
    turtle.penup()
    turtle.back(length)
    turtle.pendown()


def coloredPythagorasTree(turtle, screen, level, max_level, length):
    # Break condition
    if level == 0:
        return

    if abs(max_level - level) > 8:
        screen.tracer(0, 0)
    else:
        screen.update()

    # ||======||
    # || KNOT ||
    # ||======||
    coloredSquare(turtle, length)
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()

    # ||================||
    # || BRANCH DRAWING ||
    # ||================||
    branch_length = int(length / sqrt(2))

    # Left branch
    turtle.left(45)
    coloredPythagorasTree(turtle, screen, level - 1, max_level, branch_length)

    # Right branch
    turtle.right(90)
    turtle.penup()
    turtle.forward(branch_length)
    turtle.pendown()
    coloredPythagorasTree(turtle, screen, level - 1, max_level, branch_length)
    turtle.penup()
    turtle.back(branch_length)
    turtle.pendown()

    # Return to correct point and angle to have correct recursion
    turtle.left(45)
    turtle.penup()
    turtle.back(length)
    turtle.pendown()


def setupTurtle(h, length, n, screen, turtle):
    screen.title("Pythagore tree n=" + str(n))
    screen.delay(0)
    turtle.ht()
    turtle.speed('fastest')
    turtle.penup()
    turtle.goto(-length / 2, -h / 2)
    turtle.pendown()
    turtle.right(270)


def main():
    length = 150
    n = 8
    h = length/0.3 * (1-pow(sqrt(2), -n))

    # Setup turtle
    turtle = Turtle()
    screen = Screen()
    setupTurtle(h, length, n, screen, turtle)

    if n <= 12:
        coloredPythagorasTree(turtle, screen, n, n, length)
        # pythagorasTree(turtle, n, n, length)
    else:
        screen.title("PLEASE WAIT 20sec")
        screen.tracer(0, 0)
        # coloredPythagorasTree(turtle, screen, n, n, length)
        pythagorasTree(turtle, n, n, length)
        screen.title("Pythagore tree n=" + str(n))
        screen.update()
    screen.exitonclick()


if __name__ == '__main__':
    main()
