# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 4

#Develop a program that determines if a given year is a leap year or not and prints the result.

number = int(input("Enter a year:"))

if number % 4 == 0:
    print(f"{number} is a leap year")
else:
    print(f"{number} is not a leap year!")
