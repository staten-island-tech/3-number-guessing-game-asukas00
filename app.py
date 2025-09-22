import random

answer = random.randint(1,10)
guess = (input("guess a number between 1-10"))

if guess >= answer:
    print("your number is too high")
elif guess == answer:
    print("you got it")
elif guess <= answer:
    print("your number is too low")