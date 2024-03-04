rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

game_images = [rock, paper, scissors]


userOption = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if userOption >= 3 or userOption < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[userOption])

    machineOption = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[machineOption])


    if userOption == 0 and machineOption == 2:
        print("You win!")
    elif machineOption == 0 and userOption == 2:
        print("You lose!")
    elif machineOption > userOption:
        print("You lose!")
    elif userOption > machineOption:
        print("You win!")
    elif userOption == machineOption:
        print("You had a draw")

