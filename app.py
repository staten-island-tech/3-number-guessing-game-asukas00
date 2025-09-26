import random

answer = random.randint(1,10000)
print("guess a number between 1-10000")
attempt = 0
guess_history = []
while True:
        guess = int(input("Enter your guess: "))
        
        if guess < answer:
            print("Too low. Try again.")
            attempt += 1
            guess_history.append(guess)
            print(guess_history)
        elif guess > answer:
            print("Too high. Try again.")
            attempt += 1
            guess_history.append(guess)
            print(guess_history)
        else:
            attempt += 1
            print(f"YAY! you got it in {attempt} attempts!")
            guess_history.append(guess)
            print(guess_history)
            break
