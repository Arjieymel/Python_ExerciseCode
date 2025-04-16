# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 5

#Develop a program that calculates the factorial of a given number using a for loop and prints the result.

number = int(input("Enter a number:"))

num = 1

if number < 0:
    print("invalid")
else:
    for i in range(1, number + 1):
        num *= i
    print(f"The factorial of {number} is {num}")