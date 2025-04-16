# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 4

#Create a program that checks if a given string is a palindrome or not and prints the result.

text = input("Enter a word: ")

if text == text[::-1]:
    print(f"{text} is a palindrome!")
else:
    print("Not a palindrome.")
