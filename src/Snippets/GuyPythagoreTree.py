# ||======================================================================================================||
# || NOT MINE: SOURCE : https://www.mathweb.fr/euclide/2019/03/19/python-turtle-et-un-arbre-de-pythagore/ ||
# ||======================================================================================================||

from turtle import forward, left, right, back, pencolor, fillcolor, begin_fill, end_fill, pendown, penup, speed, exitonclick
import math
from random import uniform


def change_color():
    return uniform(0, 1), uniform(0, 1), uniform(0, 1)


def tree(s):
    if s < 5:
        return
    square(s)
    forward(s)
    s1 = s / math.sqrt(2)
    left(45)
    tree(s1)
    right(90)
    forward(s1)
    tree(s1)
    back(s1)
    left(45)
    back(s)


def square(s):
    e1, e2, e3 = change_color()
    fillcolor(e1, e2, e3)
    begin_fill()
    for i in range(4):
        forward(s)
        right(90)
    end_fill()


if __name__ == '__main__':
    speed('fastest')
    pencolor("white")
    N = 9  # CURRENT MAX WITH a = 100
    a = 200
    h = a/0.3 * (1-pow(2, -N/2))
    penup()
    left(180)
    format(a/2)
    left(90)
    forward(h/2)
    left(-90)
    right(90)
    pendown()
    tree(a)
    exitonclick()
