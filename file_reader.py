# 4. File Reader
# Task:
#  Ask the user for a filename and try to open it.
# If the file doesn’t exist → handle FileNotFoundError
# If it exists → print its content
# :memo: Hint: Use open(filename, "r")

file_name=input("Enter the file name:")
try:
    with open (file_name,"r")as file:
        content =file.read()
        print("THE file contents")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
        