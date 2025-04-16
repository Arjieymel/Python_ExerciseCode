# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 3

#Create a program that reads a string representing a boolean value ('1' for True, '0' for False), 
# converts it to an integer data type (1 for True, 0 for False), and displays both the original 
# string and the converted integer along with their data types.

value = input("Enter a boolean value as as string ('1' for  True, '0' for False)")
print(f"Original string value: '{value}', Data type: {type(value)}")

converted = int(value)
print(f"Converted integer value: {converted}, Data type: {type(converted)}")
