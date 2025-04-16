# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 4

#Create a program that checks if a given character is a vowel or a consonant and prints the result.

vowels = input("Enter a character (A to Z):").lower()

vowel = "aeiou"

if vowels in vowel:
    print(f"{vowels} is a vowel")

else:
    print(f"{vowels} is a consonant")
