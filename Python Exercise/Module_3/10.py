# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 3

#Create a program that reads a string and counts the number of vowels (a, e, i, o, u) in it.

words = input("Enter a string: ").lower()
vowels = {'a', 'e', 'i', 'o', 'u'}
vowel = 0

for char in words.lower():
    if char in vowels:
        vowel += 1

print(f"Number of vowels: {vowel}")


