import random
import os
import time

def rolldice(side):
    number = random.randint(0, side)
    return number

def health():
    health = (rolldice(6)*rolldice(12)/2)+10
    print("Health:", health)
    return health
  
def strength():
    strength = (rolldice(6)*rolldice(12)/2)+12
    print("STRENGTH:", strength)
    return strength
    
print("⚔️ BATTLE TIME ⚔️")
print()

character1Name=input("Name your Legend \n")
character1Type=input("\nCharacter Type (Human, Elf, Wizard, Orc):\n")

print()
print(character1Name)
character1Health = health()
character1Strength=strength()
print()

print("Who are they battling?\n")

character2Name=input("Name your Legend \n")
character2Type=input("\nCharacter Type (Human, Elf, Wizard, Orc):\n")

print()
print(character2Name)
character2Health = health()
character2Strength=strength()


print("⚔️ BATTLE TIME ⚔️")
print()

while True:
    rounds=1
    time.sleep(1)
    os.system("clear")
    print("⚔️ BATTLE TIME ⚔️")
    print()
    print("The battle begin!")
    print()
    character1 = rolldice(10)
    character2 = rolldice(10)

    damage=abs((character1Strength-character2Strength)+1)

    if character1 > character2:
        character2Health = character1Health - damage
        print(character1Name, "wins the blow")
        print(character2,"take a hit, with",damage,"damage")

      
    elif character1 < character2:
        character1Health = character1Health - damage
        print(character2Name, "wins the blow")
        print(character1,"take a hit, with",damage,"damage")
    else:
         print("It's a Tie")

    print(character1Name,"\nHealth",character1Health)
    print(character2Name,"\nHealth",character2Health)
    print()
    winner = None

    if character2Health<=0:
        
        os.system("clear")
        print(character1Name,"destroyed",character2Name,"in",rounds,"round")
        winner = character2Name
        time.sleep(2)
        break
    elif character1Health<=0:
        print(character2Name,"destroyed",character1Name,"in",rounds,"round")
        winner = character2Name
        time.sleep(2)
        break
    else:
        print("\nAnd they're both standing for the next round!")
        rounds=+1
        time.sleep(4)
        

time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner,"has Won")

