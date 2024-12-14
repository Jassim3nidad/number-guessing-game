import random

number = random.randint(1, 100)

print("Welcome to random number guessing game!")
print("You have 5 tries! guess carefully")
print("Enter a number between(1-100)")
tries = 1
max_tries = 5
is_running = True

while is_running and tries <= max_tries:
    guess = input(f"Enter your guess (1-100) - Attempt {tries}/{max_tries}: ")
    
    if guess.isdigit():
        guess = int(guess)
        tries += 1
        if guess < 1 or guess > 100:
            print("That number is out of range")
            print("Select a number between 1-100")
        elif guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! The answwer was {number}")
            is_running = False
            
    else:
        print("Invalid input, Enter a number!")
    if tries > max_tries:
        print(f"You've used all {max_tries} tries. The correct number was {number}. Better luck next time!")
        is_running = False