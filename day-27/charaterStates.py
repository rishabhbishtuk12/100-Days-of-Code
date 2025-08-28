import os
import random
import time

def rollDice(side):
    result = random.randint(1, side)
    return result

def health():
    health = ((rollDice(6)*rollDice(12))/2)+10
    print("HEALTH:",health)

def strength():
    strength=((rollDice(6)*rollDice(8))/2)+12
    print("STRENGTH:",strength)

while True:

    os.system("clear")
    print("CHARACTER BUILDER")
    print()
    time.sleep(2)
    nameInput=input("Name your Legend:\n")
    charInput=input("\nCharacter type (Human, Elf, Wizard, Orc):\n")
    print()
    print(nameInput,"\n")
    health()
    strength()
    print("\nMay your name go down in Legend...\n")
    restart=input("Again?: ")
    if restart=="yes" and "Yes":
        continue
    else:
        break

