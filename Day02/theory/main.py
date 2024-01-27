#Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings

#Python primitive Data type
#string, there are some action we can do with string, one of them is pull out each caracter indivially
print("Hello"[0])
print("123" + "123")

#integer (no decimal), if the number is kept inside doble quote, it is not treated as number.
print(123 + 123)
print(123_987_459) #the underscores when used with numbers are seen as coma in Python

#Float
print(3.14159)

#Boolean
print(False)
print(True)




#Type Conversion
random_number = 1235489
number_to_string = str(random_number)
print(type(number_to_string))




#Mathematical Operations in Python
adding = 3 +5
substraction = 7 + 4
multiplication = 3 * 2
diviion = 6 / 3 #Division always end up with a float number
exponents = 2 ** 2

#PRIORITIES
#Parentheses
#Exponents
#Multiplicaiton / #Division
#Addition / #Subtraction




#Round the Number, instead of transforming the number to integer, we can round it
print(round(8 / 3))
print(round(8 / 3, 2)) #If I want to specify how many numbers




#Floor division, we use this one when we want an Integer instead of Float as the result of the divison
print(8 // 3)




#When we add the result of one equation into a variable and continue calculating that number with other numbers, we can calculate and attribute the result to that same variable without repeating code.
result = 8 / 2
result /= 2
print(result)

score = 5 #This is very handy when we have to manipulate one variable based on its previous value.
score += 4
print(score)




#F-string, it is extremely handy when we want to mix string with different data types (you can mix string with integer for example)
score = 0
height = 1.8
isWining = True
print(f"Your score {score}, your height is {height}, you are wining is {isWining}")
