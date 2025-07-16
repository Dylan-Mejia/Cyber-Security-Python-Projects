import string 
import getpass

def check_passwrd():
    password = getpass.getpass("Enter your password: ")
    strength = 0
    feedback = ''

    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1
            
    if lower_count >= 1:
        strength += 1  
    if upper_count >= 1:
        strength += 1  
    if num_count >= 1:
        strength += 1  
    if wspace_count >= 1:
        strength += 1  
    if special_count >= 1:
        strength += 1  

    if strength == 1:
        feedback = "Your password is very weak! Use a stronger password."
    elif strength == 2:
        feedback = "Your password is weak! Use a stronger password."
    elif strength == 3:
        feedback = "Your password is ok! But it can be better."
    elif strength == 4:
        feedback = "Your password is good! It can be pretty hard to guess."
    elif strength == 5:
        feedback = "Your password is very strong! It is almost impossible to guess!"

    print("")
    print("Your password has: ")
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")
    print("")
    print(f"Password Strength: {strength}")
    print(f"Feedback: {feedback}")


print("Welcome to Password Strength Checker!")
check_passwrd()
