#Day 3 - Beginner - Control Flow and Logical Operators

# > Grater than
# < Less than
# >= Grater or equal than
# <= Less or equal than
# == equal than
# != Not equal to
    
#Normal if
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120: 
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")




#Nested if statement with elif
#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))

if height >= 120: 
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")





#Multiple if, when we use if / elif / else, only one condition will be fulfilled, however, when we use Multiple if, we can validade multiple conditions.
bill = 0
if height >= 120: 
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12
    
    wants_photo = input("Do you want a photo taken? Y or N ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")