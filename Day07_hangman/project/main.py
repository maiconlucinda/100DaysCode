import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

guess = input("Guess a letter: ").lower()



for letter in chosen_word:
    if letter == guess:
        print("True")
    else:
        print("False")


        


