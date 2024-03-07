

# For Loop (we can go through each item in a list and perform some action with each individual item)
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")



# Loops with fuction range(), this fucntion helps us to set a starter and an end
total = 0
for number in range(1, 101):
    total += number

print(total)