import random

words = ["Minecraft", "Mario"]

word = random.choice(words).lower()

display_word = len(word) * "_"
letters_choosen = []
choices_left = 6

while True:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(display_word)
    print(f"letters chosen: {letters_choosen}")
    print(f"choices left: {choices_left}")

    user_input = input("> ").lower()
    if len(user_input) != 1:
        continue

    if user_input in letters_choosen:
        continue
    else:
        letters_choosen.append(user_input)

    if user_input in word:
        for i in range(len(word)):
            if word[i] == user_input:
                display_word = list(display_word)
                display_word[i] = user_input
                display_word = "".join(display_word)
    else:
        choices_left -= 1

    if display_word == word:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(display_word)
        print("You win")
        break

    if choices_left == 0:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(display_word)
        print("You lose")
        break
