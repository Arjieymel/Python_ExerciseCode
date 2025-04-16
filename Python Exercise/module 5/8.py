# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 5

#Create a program that prints the multiplication table of a given number using a for loop.

number = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
