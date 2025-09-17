# question

#  Ask the user for their age.
# If the input is not a number → handle ValueError
# If the age is negative → raise and handle your own ValueError with a message "Age cannot be negative."
# :memo: Hint: Use if age < 0: raise ValueError(...)


def age_validate():
    while True:
        try:
            age_str = input("Enter an age:")
            age = int(age_str)
        
            if age <0:
                raise ValueError("Age cannot be negative")
            else:
                print(f"Your age is,{age}")
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid non-negative number for your age.")
age_validate()


# with out try and except
 
# age_str = int(input("Enter an age:"))
# # age = int(age_str)
        
# if age_str <0:
#     raise ValueError("Age cannot be negative")
# else:
#     print(f"Your age is,{age_str}")       
    