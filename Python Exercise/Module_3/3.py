# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 3

#Develop a program that reads a boolean value as a string ('True' or 'False'), 
# converts it to a boolean data type, and displays both the original string and the 
# converted boolean along with their data types.

value = input("Enter a boolean value as a string ('True' or 'False')").lower()
print(f"Original string value: {value}, Data type: {type(value)}")

converted = bool(value)
print(f"Converted boolean value: {converted}, Data type: {type(converted)}")

