import random

valid_choices = ["rock", "paper", "scissors"]


def ai_won():
    print(f"AI won! AI chose {ai_choice}")


def player_won():
    print(f"Player won! AI chose {ai_choice}")


while True:
    ai_choice = random.choice(valid_choices)

    user_input = input("> ")
    if user_input not in valid_choices:
        print("Try again")
        continue

    elif user_input == "rock":
        if ai_choice == "paper":
            ai_won()
        elif ai_choice == "scissors":
            player_won()
    elif user_input == "paper":
        if ai_choice == "rock":
            player_won()
        elif ai_choice == "scissors":
            ai_won()
    elif user_input == "scissors":
        if ai_choice == "paper":
            player_won()
        elif ai_choice == "rock":
            ai_won()
