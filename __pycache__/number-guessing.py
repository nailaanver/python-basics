# Build a Number Guessing Game (random number 1–100, user keeps guessing until correct).

import random
def number_guessing_game():
    secret_number = random.randint(1,100)
    print(f"(For testing) Secret number is: {secret_number}") 
    max_attempts = 10
    guess = 0
    attempt = 3
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    
    while guess != secret_number and attempt < max_attempts:
        try:
            guess = int(input("Enter Your Guess:"))
            attempt += 1
            if guess < secret_number:
                print("Its too low,Try again")
            elif guess > secret_number:
                print("Its too High,Try again")
            else:
                print(f"Congratulation,you guess the number {secret_number} in {attempt} attempt")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    if guess != secret_number:
        print(f"Sorry! You've used all {attempt} attempts. The number was {secret_number}.")
number_guessing_game()