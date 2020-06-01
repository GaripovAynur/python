import turtle

turtle.speed(1)
count = int(0)


def kvadrat(x, y):
    for i in range(4):
        turtle.forward(x)
        turtle.left(y)


kvadrat(100, 90)
turtle.goto(150, 150)
kvadrat(100, 90)
