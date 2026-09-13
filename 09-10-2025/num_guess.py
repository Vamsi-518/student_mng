import random
num = random.randint(1, 10)
for _ in range(3):
    guess = int(input("Guess number (1–10): "))
    if guess == num:
        print(" Correct!")
        break
    else:
        print("Try again!")