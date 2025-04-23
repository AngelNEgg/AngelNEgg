# Angel Nazaire
# 4/22/2025
# Period 2
'''Video Game Coding Assignment/Project: Create your game on scratch, 
or another free coding platform of your choice.  
Your game must include instructions/directions, and 
a final objective. (Still a work in progress)'''

# Russian Roulette-Like Game

# Imports
import random
import time
import simplegui

# Variables
health = 3
oppHealth = 3
shell1 = random.randint(0,1)
shell2 = random.randint(0,1)
shell3 = random.randint(0,1)
shell4 = random.randint(0,1)
shell5 = random.randint(0,1)
rounds = random.randint(2,5)
chamber = 0
item = " "
score = 0

# Functions
def itemFunc():
    item = random.randint(1,4)
    if item == 1:
        item = "Phone"
        print("Item:",item)
        return item
    elif item == 2:
        item = "Eyeglass"
        print("Item:",item)
        return item
    elif item == 3:
        item = "Double Down"
        print("Item:",item)
        return item
    else:
        item = "Soda"
        print("Item:",item)
        return item

def turnFunc():
    shell1 = random.randint(0,1)
    shell2 = random.randint(0,1)
    shell3 = random.randint(0,1)
    shell4 = random.randint(0,1)
    shell5 = random.randint(0,1)
    chamber = (shell1+shell2+shell3+shell4+shell5)
    if chamber == 0 or chamber == 5:
        turnFunc()
        return
    else:
        print(f"{chamber} Live, {5-chamber} Blank.")
        return
    
# Gameplay
print("Tutorial: Five shells are in play, and you can decide to...\n\t-'Choose Self': Guessing 'live' will result in you loosing a health point.\n\t-'Choose Opponent': Guessing 'blank' will result in the end of your turn.\n\t-'Use Item': Using an item will remove it from your inventory, and can only be\n\t replenished at the start of a round.")
turnFunc()
itemFunc()

# Gameplay Functions
def shell1Func():
    choice = input("What will you do? ")
    if choice == "Choose Self" and shell1 == 1:
        time.sleep(2)
        print("You lost a health point.")
        chioce = input(("Do you want to use an item? "))
        if choice == "Yes" and item == 4:
            item = 0
            turnFunc()
            shell2Func()
        elif choice == "Yes" and item != 4:
            print("You don't have healing items.")
            pass
        else:
            print("Understood. Moving on, then.")
            turnFunc()
            shell2Func()
            pass
        
    elif choice == "Choose Self" and shell1 == 0:
        time.sleep(2)
        print("The shell was blank.")
        score += 1
        shell2Func()
    
def shell2Func():
    choice = input("What will you do? ")
    if choice == "Choose Self" and shell1 == 1:
        time.sleep(2)
        print("You lost a health point.")
        chioce = input(("Do you want to use an item? "))
        if choice == "Yes" and item == 4:
            item = 0
            turnFunc()
            #shell3Func()
        elif choice == "Yes" and item != 4:
            print("You don't have healing items.")
            pass
        else:
            print("Understood. Moving on, then.")
            turnFunc()
            #shell3Func()
            pass
        
    elif choice == "Choose Self" and shell2 == 0:
        time.sleep(2)
        print("The shell was blank.")
        score += 1
        #shell3Func()
        
shell1Func()
