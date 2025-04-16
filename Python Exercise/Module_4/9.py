# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 4

#Develop a program that determines if a given number is a prime number or not and prints the result.

number = int(input("Enter a number:"))

if number % 2 == 0:
    print(f"{number} is not a prime number")
else:
    print(f"{number} is a prime number")