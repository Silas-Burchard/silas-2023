import random
from colorama import Fore, Back

while True:
    user_action = input(Fore.BLACK+Back.LIGHTWHITE_EX+"Enter a choice (punch, kick, shield): ")
    possible_actions = ["punch", "kick", "shield"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. draw!")
    elif user_action == "punch":
        if computer_action == "kick":
            print("punch kills kick! that brat is dead!")
        else:
            print("shield blocks punch! game over.")
    elif user_action == "kick":
        if computer_action == "shield":
            print("kick kills shield! that brat is dead!")
        else:
            print("kick kills shield!  game over.")
    elif user_action == "shield":
        if computer_action == "punch":
            print("shield kills punch! that brat is dead!")
        else:
            print("shield kills punch!  game over.")
    play_again = input("Play again? (y/n)")
    if play_again.lower() != "y":
        print("K, bye!")
        break
