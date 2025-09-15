# :memo: Question 1: ATM System (OOP)
# Question:
#  Write a Python program using Object-Oriented Programming (OOP) concepts to create a simple ATM system.
# Requirements:
# Create a class Account with:
# Private data members: account_number, holder_name, balance
# Methods to:
# deposit money
# withdraw money
# check balance
# show account details
# Create a class ATM that inherits from Account and adds:
# A private data member pin
# A method validate_pin() to check the entered PIN
# Override show_details() to show ATM account details (polymorphism)
# In the main program:
# Create an object of the ATM class
# Ask the user to enter the PIN
# If the PIN is correct, display a menu to:
# Check balance
# Deposit money
# Withdraw money
# Show account details
# Exit
# Note:
#  Your program must demonstrate the OOP concepts of
#  Class, Object, Encapsulation, Inheritance, and Polymorphism.


class Account:
    def __init__(self,account_number, holder_name, balance):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print("Depposit successfull,New balance is:",self.__balance)
        else:
            print("Deposit amount must be positive")
    def withdraw(self,amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print("Cash withdraw successfully,New balnce is:",self.__balance)
            else:
                print("Insuffifciant funds")
        else:
            print("Withdrawel amount must be positive")
    def check_balance(self):
        return self.__balance
    def show_details(self):
        print("/n---Account Details---")
        print("Account Number:",self.__account_number)
        print("Account Holder Name:",self.__holder_name)
        print("Balance:",self.__balance)
        
class ATM(Account):
    def __init__(self, account_number, holder_name, balance,pin):
        super().__init__(account_number, holder_name, balance)
        self.__pin = pin
        
    def validate_pin(self, entered_pin):
        return self.__pin == entered_pin
    def show_details(self):
        super().show_details()
        print("ATM Account Details")
        print("PIN is secured and not displayed")
    