from colorama import Fore
import random

words = [
    "seize",
    "serve",
    "vader",
]

chances = 5
word = random.choice(words)
won = False

while chances > 0:
    user_input = input("> ")
    if len(user_input) != 5:
        continue
    chances -= 1

    checks = 0
    output = [None, None, None, None, None]
    for user_i in range(len(user_input)):
        for word_i in range(len(word)):
            char = list(user_input)[user_i]
            if list(user_input)[user_i] == list(word)[word_i]:
                if user_i == word_i:
                    output[user_i] = {"color": Fore.GREEN, "char": char}
                else:
                    output[user_i] = {"color": Fore.YELLOW, "char": char}
            else:
                output[user_i] = {"color": Fore.RESET, "char": char}

    out_str = ""
    for o in output:
        out_str += f"{o['color']}{o['char']}"

    print(out_str)
    print(f"{chances} chance(s) left!")

    if user_input == word:
        won = True
        chances = 0

if won:
    print("You Win!")
else:
    print("You Lose!")
