import random

print("Welcome to the Number Guessing Game!")
print("The computer will choose a number from 1 to 100. Try to guess it in 3 tries.\n")

number = random.randint(1, 100)

for i in range(3):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed the right number ")
        break
    elif guess < number:
        print("Your guess is lower than the real number.\n")
    else:
        print("Your guess is higher than the real number.\n")

if guess != number:
    print("No more tries! The correct number was:", number)
