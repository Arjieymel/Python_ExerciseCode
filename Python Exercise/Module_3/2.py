# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 3

#PCreate a program that reads an integer, converts it to a string, 
# and displays both the original integer and the converted string along with their data types.

number = int(input("Enter an integer:"))
print(f"Original integer value: {number}, Data type: {type(number)}")

converted = str(number)
print(f"Coverted string value: '{converted}', Data type: {type(converted)}")

