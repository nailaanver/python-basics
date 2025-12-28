# Design a Password Strength Checker that evaluates a given password.

import re
def check_password_strength(password):
    strength_score = 0
    suggetions = []
        # Criteria 1: Length
    if len(password) < 8:
        suggetions.append("Password should be atleast 8 characters long")
    elif len(password) < 12:
        strength_score +=1
        suggetions.append("Consider making your password longer for best secuirity")
    else:
        strength_score +=2
        
         # Criteria 2: Uppercase letters
    if re.search(r"[A-Z] ",password):
        strength_score +=1
    else:
        suggetions.append("Include atleast one uppercase letter")
         # Criteria 2: Lowercase letters
    if re.search(r"a[-z] ",password):
        strength_score +=1
    else:
        suggetions.append("Include atleast one lowercase letter")
    # Determine strength level based on score
    
    if strength_score < 2:
        strength = "Weak"
    elif strength_score < 4:
        strength = "Medium"
    elif strength_score < 6:
        strength = "Strong"
    else:
        strength = "Very strong"
    return strength,suggetions

while True:
    password = input("Enter your password (or 'quit' to exit): ")
    if password.lower() == 'quit':
        break
    strength, suggestions = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    if suggestions:
            print("Suggestions for improvement:")
            for suggestion in suggestions:
                print(f"- {suggestion}")
    else:
            print("Your password meets all recommended criteria!")
    print("-" * 30)