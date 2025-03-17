import random
target = random.randint(10, 20)
while True:
    guess = int(input("Guess a number between 10-20: "))
    if guess == target:
        print("Congratulations! You guessed it!")
        break
    else:
        print("Try again!")
