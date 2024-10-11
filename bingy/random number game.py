import random

ran_number = random.randint(1,100)
correct_guess = False

while correct_guess == False:
    guess_number = int(input("Guess a number between 1-100: "))
    if ran_number < guess_number:
        print("Your guess was too high, guess lower.")
    else:
        print("Your guess was too low, guess higher.")
    
    if ran_number == guess_number:
        correct_guess = True

print("Your guess was correct!")