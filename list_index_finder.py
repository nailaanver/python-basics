# 3. List Index Finder
# Task:
#  Create a list: numbers = [10, 20, 30, 40].
#  Ask the user to enter an index number.
# Print the value at that index.
# Handle:
# IndexError if the index is out of range
# ValueError if the input is not an integer

numbers = [10, 20, 30,40]

try:
    index_str = input("Enter an index number:")
    index = int(index_str)
    if 0 <= index < len(numbers):
        print(f"The value of index is:{numbers[index]}")
    else:
        print("Index is out of range")
except ValueError:
    print("Error:Invalid input.please enter an integer")
    
        
