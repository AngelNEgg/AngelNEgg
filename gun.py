# Russian Roulette

import random

shell1 = random.randint(0,1)
shell2 = random.randint(0,1)
shell3 = random.randint(0,1)
shell4 = random.randint(0,1)
shell5 = random.randint(0,1)

item = random.randint(1,4)
if item == 1:
    item = "Phone"
elif item == 2:
    item = "Eyeglass"

print("Choices:\n\tShoot Self: Guessing 'live' will result in you loosing a health point.\n\tShoot Dealer: Guessing 'blank' will result in the end of your turn.\n\tUse Item: Using an item will remove it from your inventory, and can only be\n\treplenished at the start of a round.")

choice = input("What will you do?")
