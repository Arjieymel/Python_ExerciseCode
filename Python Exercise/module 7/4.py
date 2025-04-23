# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 7
#Create a program that defines a list of student names and allows the user to search for a student by entering their name. If the student is found, print "Student found", otherwise print "Student not found".

name = ['rosemarie', 'rjmel', 'april', 'romelyn']

seacrh = input("Enter a StudentName to Search:").lower()

if seacrh in name:
    print("Student Name Found")
else:
    print("Student Name Not Found!")