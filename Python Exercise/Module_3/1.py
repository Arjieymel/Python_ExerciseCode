# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 3

#Write a program that reads a string representing a floating-point number and converts it to an integer, 
# then prints the integer value.

number = input("Enter a floating-point number as a string:")
print(f"Original string value: {number}, Data type: {type(number)}")

num1 = float((number))
print(f"Converted float value: {num1}, Data type:{type(num1)}")
