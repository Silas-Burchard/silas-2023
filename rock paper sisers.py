import random
import turtle
from colorama import Fore, Back 

name = input("what is your name? ")
answer = input("hi " + name + " want to play rock paper scissors? (yes/no) ")
if answer == "no":
    print("I QUIT!!!!!!!!!")
    quit()
else:
    print("yay yahoo")

win = 0
loss = 0
games = 0
while games < 3:
    user_action = input(Fore.BLACK+Back.LIGHTWHITE_EX+"Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            win += 1
            games += 1
        else:
            print("Paper covers rock! You lose.")
            loss += 1
            games += 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            win += 1
            games += 1
        else:
            print("Scissors cuts paper! You lose.")
            loss += 1
            games += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            win += 1
            games += 1
        else:
            print("Rock smashes scissors! You lose.")
            loss += 1
            games += 1
if loss > win:
    print("you lose over all")
    quit()

else:
    print("you win over all")
    t = turtle.Turtle()
    t.speed(0)


    def pen(color):
        t.color(color)


    pen('red')


    def move():
        t.pu()
        x = random.randint(-165, 165)
        y = random.randint(-165, 165)
        t.goto(x, y)
        t.pd()


    def sky(colour):
        wn = turtle.Screen()
        wn.bgcolor(colour)


    sky('black')


    def firework(size):
        for num in range(20):
            t.fd(size)
            t.rt(180 - (360 / 20))


    firework(50)
    move()
    pen('yellow')
    firework(75)
    move()

    pen('orange')
    firework(199)
    firework(50)
    move()

    pen('blue')
    firework(75)
    move()

    pen('pink')
    firework(199)
    firework(50)
    move()

    pen('yellow')
    firework(75)
    move()

    pen('orange')
    firework(199)
    firework(50)
    move()

    pen('blue')
    firework(75)
    move()

    pen('pink')
    firework(199)
    firework(50)
    move()

    pen('yellow')
    firework(75)
    move()

    pen('orange')
    firework(199)
    firework(50)
    move()
    pen('blue')
    firework(75)
    move()

    pen('pink')
    firework(199)
    firework(50)
    move()

    pen('yellow')
    firework(75)
    move()

    pen('orange')
    firework(199)
    firework(50)
    move()

    pen('blue')
    firework(75)
    move()

    pen('pink')
    firework(199)

