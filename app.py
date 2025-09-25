import random

answer = random.randint(1,10)
print("guess a number between 1-10")
attempt = 0
guess = int(input("Enter a number"))
while True:
    
    if guess > answer:
        print("your number is too high")
        attempt += 1
    elif guess < answer:
        print("your number is too low")
        attempt += 1
    else:
        attempt += 1
        print("You got it in {attempts}!")
        break
