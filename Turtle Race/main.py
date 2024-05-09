import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_guess = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "orange", "yellow", "blue", "purple"]
start_positions = [-80, -50, -20, 10, 40, 70]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_guess:
                print(f"You win! The winning turtle is {winning_turtle}")
            else:
                print(f"You lose! The winning turtle is {winning_turtle}")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
