a_str = input("Enter the first number:")
b_str = input("Enter the second number:")
try:
    a = int(a_str)
    b = int(b_str)
    divide = a/b
    print("Result of divition is",divide)
except ValueError:
    print("Invalid input. Please enter numeric values only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero. Please enter a non-zero divisor.")
# except Exception as e:
#    print(f"An unexpected error occurred: {e}")