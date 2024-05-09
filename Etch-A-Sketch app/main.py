from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(50)

def move_backwards():
    tim.backward(50)

def move_counterclock():
    tim.circle(120, 100)

def move_clockwise():
    tim.circle((-120), 100)

def move_left():
    tim.left(90)

def move_right():
    tim.right(90)
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="f", fun=move_forwards)
screen.onkey(key="b", fun=move_backwards)
screen.onkey(key="a", fun=move_counterclock)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="l", fun=move_left)
screen.onkey(key="r", fun=move_right)
screen.exitonclick()