#https://realpython.com/beginners-guide-python-turtle/

import turtle
import random

turtle.title("Turtle Race")

die = [1, 2, 3, 4, 5, 6]

def player_one():
    player_one = turtle.Turtle()
    player_one.color("green")
    player_one.shape("turtle")
    player_one.penup()
    player_one.goto(-100, 100)


def player_two():
    player_two = turtle.Turtle()
    player_two.color("red")
    player_two.shape("turtle")
    player_two.penup()
    player_two.goto(-100, -100)


def player_one_finish():
    player_one.goto(300, 100)
    player_one.pendown()
    player_one.dot(50)
    player_one.penup()
    player_one.goto(-100, 100)


def player_two_finish():
    player_two.goto(300, 100)
    player_two.pendown()
    player_two.dot(50)
    player_two.penup()
    player_two.goto(-100, 100)

player_one()
player_two()
player_one_finish()
player_two_finish()

for i in range(20):
    if player_one.pos() >= (300,100):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (300,-100):
        print("Player Two Wins!")
        break
    else:
        player_one_turn = input("Press 'Enter' to roll the die ")
            die_outcome = random.choice(die)
            print("The result of the die roll is: ")
            print(die_outcome)
            print("The number of steps will be: ")
            print(20*die_outcome)
            player_one.fd(20*die_outcome)
            player_two_turn = input("Press 'Enter' to roll the die ")
            d = random.choice(die)
            print("The result of the die roll is: ")
            print(die_outcome)
            print("The number of steps will be: ")
            print(20*die_outcome)
            player_two.fd(20*die_outcome)

turtle.Screen().exitonclick()

