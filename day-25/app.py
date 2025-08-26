import random
def rollDice(side):
    side=random.randint(1, side)
    return side
def side6and8():
    side6 = rollDice(6)
    side8 = rollDice(8)
    hp=side8*side6
    print("The health is",hp,"hp")

print("CHARACTER STAT GENERATOR")
print()
ask ="yes"
while ask =="yes":
    input("Name your warrior: ")
    side6and8()
    print()
    ask=input("Want to create another character? ")
    



