import random

secret = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 to 100")

while attempts < 7:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"You won in {attempts} attempts! Score: {100 - attempts*10}")
        break
else:
    print(f"Game over! Number was {secret}")