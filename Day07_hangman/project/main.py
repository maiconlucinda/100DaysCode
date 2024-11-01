import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


word_length = len(chosen_word)
display = ["_"] * word_length
print(display)


letter = ""
lives = 5


while "_" in display:
    guess = input("Guess a letter: ").lower()
    correct_guess = False

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            correct_guess = True

    if correct_guess:
        print(f"Bom palpite!")


    if not correct_guess:
        lives -= 1
        print(f"Palpite incorreto! Você ainda tem {lives} tentativas restantes.")

    if lives == 0:
        print("Suas vidas acabaram, você perdeu.")
        break

    print(" ".join(display))


if not "_" in display:
    print("Parabéns, você ganhou")

    




        


