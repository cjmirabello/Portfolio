import random

highest_number = input("Type a number: ")

if highest_number.isdigit():
    highest_number = int(highest_number)

    if highest_number <= 0:
        print("Please select a number higher than 0 next time")
        quit()
else:
    print("Please type in a number next time")
    quit()

random_number = random.randint(0, highest_number)
guesses = 0

while True:
    guesses += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type in a number next time")
        continue

    if guess == random_number:
        print("That is the correct number!")
        break
    elif guess > random_number:
        print("The number is higher.")
    else:
        print("The number is lower")

print("it took you", guesses, "guesses")
