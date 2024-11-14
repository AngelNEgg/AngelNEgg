# Russian Roulette

import random

shell1 = random.randint(0,1)
shell2 = random.randint(0,1)
shell3 = random.randint(0,1)
shell4 = random.randint(0,1)
shell5 = random.randint(0,1)
rounds = random.randint(2,5)

item = random.randint(1,4)
if item == 1:
    item = "Phone"
elif item == 2:
    item = "Eyeglass"
elif item == 3:
    item = "Knife"
else:
    item = "Cigarette"

print("Choices:\n\t-Shoot Self: Guessing 'live' will result in you loosing a health point.\n\t-Shoot Dealer: Guessing 'blank' will result in the end of your turn.\n\t-Use Item: Using an item will remove it from your inventory, and can only be\n\t replenished at the start of a round.")

health = 3
choice = input("What will you do? ")

def turnFunc():
    shell1 = random.randint(0,1)
    shell2 = random.randint(0,1)
    shell3 = random.randint(0,1)
    shell4 = random.randint(0,1)
    shell5 = random.randint(0,1)
    rounds = random.randint(2,5)
    if choice == "Shoot Self" and shell1 == 1:
        print("You Died? That's too bad...")
        chioce = input(("Would you like another try? "))
        if choice == "yes":
            turnFunc()
        else:
            print("I'll be seeing you, then.")
    
    
