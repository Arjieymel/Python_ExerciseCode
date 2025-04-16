# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 4

#Write a program that calculates the sum of all the numbers from 1 to a given number.

number = int(input("Enter a number:"))

num = 0

for i in range(1, number + 1):
    num += i
print("The sum of the number from 1 to", number, "is", num)