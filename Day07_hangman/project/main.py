import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = (len(chosen_word) * "_ ")
print(placeholder)

guess = input("Enter a letter: ").lower()


display = ""



for letter in chosen_word:
    if letter == guess:
        print("True")
    else:
        print("False")