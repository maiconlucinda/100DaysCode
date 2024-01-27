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



#Instead of using the function int, we might also use round
print(round(8 / 3))
#If i want to specify how many numbers
print(round(8 / 3, 2))



score = 5
#This is very handy when we have to manipulate one variable based on its previous value.
score += 4
print(score)

print("Your score is " + str(score))



#f-string
