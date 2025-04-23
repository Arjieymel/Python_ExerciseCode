def checkSum(integer):
    digit_sum = sum(int(digit) for digit in str(integer))

    # Check if the sum is even or odd using %
    return "Even Sum" if digit_sum % 2 == 0 else "Odd Sum"





print(checkSum(1234))   # Output: "Even Sum"  (1+2+3+4 = 10)
print(checkSum(567))    # Output: "Odd Sum"   (5+6+7 = 18)
print(checkSum(98765))  # Output: "Odd Sum"   (9+8+7+6+5 = 35)
print(checkSum(2468))   # Output: "Even Sum"  (2+4+6+8 = 20)
print(checkSum(13579))  # Output: "Odd Sum"   (1+3+5+7+9 = 25)
