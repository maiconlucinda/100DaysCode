import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)


display = ["_"] * word_length
letter = ""
lives = 5

while "_" in display:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        else:
            lives -= 1


    if lives == 0:
        print("Game over")
        break

    print(display)
print("Terminou")
    