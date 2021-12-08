import random
from art import logo

# Generate random number and store in a variable.
correct_guess = random.randint(1, 100)

# Store attempts remaining in a variable.
attempts_remaining = 0

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
response = input("Choose a difficulty. Type 'easy' or 'hard': ")

if response == 'easy':
    attempts_remaining = 10
else:
    attempts_remaining = 5

# Create while loop to ask user to guess random number.
while attempts_remaining > 0:
    print(f"You have {attempts_remaining} attempts left.")
    player_guess = int(input("Make a guess: "))
    if player_guess > correct_guess:
        print("Too high.")
        attempts_remaining -= 1
    elif player_guess < correct_guess:
        print("Too low.")
        attempts_remaining -= 1
    elif player_guess == correct_guess:
        print("You won!")
        break