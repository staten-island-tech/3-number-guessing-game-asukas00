""" import random

y = random.randint(1,100)
print(y)
 """
""" x = 0
while True:
    print("running")
    if x == 0:
        break """

""" import random
answer = random.randint(1,10)
guess = answer

print(input("guess a number between 1-100"))
if guess >> answer:
    print("your number is too high")
elif guess == answer:
    print("you got it")
elif guess << answer:
    print("your number is too low")
 """
import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low. Try again.")
            elif guess > number_to_guess:
                print("Too high. Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
number_guessing_game()
