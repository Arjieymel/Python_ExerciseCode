# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 4

#Create a program that checks if a given number is positive, negative, or zero and prints the result.

number = int(input("Enter a number:"))

if number < 0:
    print(f"{number} is a negative number")
elif number > 0:
    print(f"{number} is a positive number")
else:
    print("ZERO!")