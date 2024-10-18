import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


guess = input("Guess a letter: ").lower()



for letter in chosen_word:
    if letter == guess:
        print("True")
    else:
        print("False")



placeholder = (len(chosen_word) * "_ ")
print(placeholder)


display = ""
        


