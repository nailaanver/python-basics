try:
    n = int(input("Enter a number:"))
    if n<0:
        raise ValueError("Please enter a positive integer:")
    else:
        print("Valid positive number")
except ValueError :
    print("Please enter a valid input")
    