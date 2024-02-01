#Day 4 - Beginner - Randomisation and Python Lists

# Modulo Random, creating randomness
import random

# Integer
random_integer = random.randint(1, 10)
print(random_integer)

# Float
random_float = random.random()
print(random_float)

# Exemplo prático
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")




# Python List, It can have mixed data types, any type of data. And so on and so forth.
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# When we have to get an item from the Python List
print(states_of_america[5])

# To start counting from the end we could use -number
print(states_of_america[-1])

# To add a new element into our list
states_of_america.append("Maiconland")

# To add a list to another list
states_of_america.extend(["Rosiland", "Amandaland", "Ademirland", "Gracieleland"])

print(states_of_america)