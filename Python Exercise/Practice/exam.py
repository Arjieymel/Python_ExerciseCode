f_exam = int(input("1st exam: "))
s_exam = int(input("2nd exam: "))
th_exam = int(input("3rd exam: "))

# Calculate total and average
total = f_exam + s_exam + th_exam
grade = total / 3

# Print the average
print(f"Your Grade: {grade}")

# Determine pass/fail
if grade >= 75:
    print("You passed!")
else:
    print("You failed.")
