# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 7
#Create a function called count_vowels that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


print(count_vowels("Hello")) 
