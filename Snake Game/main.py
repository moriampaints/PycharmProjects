from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("THE Snake Game")

start_positions = [0, -20, -40]
all_segments = []

for square_index in range(3):
    new_segments = Turtle(shape="square")
    new_segments.color("white")
    new_segments.penup()
    new_segments.goto(x=start_positions[square_index], y=0)
    all_segments.append(new_segments)

screen.exitonclick()
