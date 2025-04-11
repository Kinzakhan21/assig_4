import random

print("Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 10)
print("I have a secret number between 1 and 10. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            break  # <-- Yeh line loop se bahar nikalne ke liye hai
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")
