# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 3

#Write a program that reads a string representing a number (integer or float), 
# converts it to a float, and displays both the original string and the converted float along with their data types.

number = input("Enter a number as string:")
print(f"Origin string value: {number}, Data type: {type(number)}")

converted = float(number)
print(f"Converted float value: {converted}, Data type: {type(converted)}")