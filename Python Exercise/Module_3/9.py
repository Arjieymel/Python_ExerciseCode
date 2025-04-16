# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 3

#Write a program that reads a string and prints its reverse.

words = input("Enter a string:")

if words == words[::-1]:
    print(f"Thw reversed of the string {words}")
else:
    print("invalid")