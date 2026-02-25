import random

number=random.randint(1, 100)

print("Guess the number between 1 and 100")

guess=int(input("Enter your guess: "))

if guess==number:
    print("Congratulations! You guessed correctly.")
else:
    if guess<number:
        print("Guess High !")
    else:
        print("Guess low !")

    print("The correct number was:", number)