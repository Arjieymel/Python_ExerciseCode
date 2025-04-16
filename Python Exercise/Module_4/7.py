# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 4

#Write a program that checks if a given number is divisible by both 5 and 7 and prints the result.

number = int(input("Enter a number:"))

if number % 5 == 0 and number % 7 == 0:
    print(f"{number} is divisible by both 5 and 7.")
else:
    print(f"{number} is not divisible by 5 and 7.")
