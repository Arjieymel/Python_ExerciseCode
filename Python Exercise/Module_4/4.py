# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 4

#Write a program that reads three numbers and prints the largest one.

number1 = int(input("Enter a first number:"))
number2 = int(input("Enter a second number:"))
number3 = int(input("Enter a third number:"))

if number1 > number2 and number1 > number3:
    print(f"{number1} is the largest number")

elif number2 > number1 and number2 > number3:
    print(f"{number2} is the largest number")

elif number3 > number1 and number3 > number2:
    print(f"{number3} is the largest number")

else:
    print("Invalid!")
