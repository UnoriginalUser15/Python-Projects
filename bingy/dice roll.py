import random

print("I am going to roll you 2 dice.")

roll_1 = random.randint(1,6)
roll_2 = random.randint(1,6)

if roll_1 == roll_2:
    print("You have rolled a double.")
else:
    print("You have not rolled a double.")

print("You have rolled the numbers", roll_1, "and", roll_2, ".")