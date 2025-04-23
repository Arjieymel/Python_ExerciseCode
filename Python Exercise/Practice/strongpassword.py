def checkPassword(password):
    
    if len(password) < 8:
        return "Weak password (must be at least 8 characters long)"

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        return "Strong password"
    else:
        return "Weak password (must contain uppercase, lowercase, and a digit)"

# Example usage:
print(checkPassword("Hello123"))  
print(checkPassword("hello123"))  
print(checkPassword("HELLO123"))  
print(checkPassword("Hello"))    
print(checkPassword("12345678")) 