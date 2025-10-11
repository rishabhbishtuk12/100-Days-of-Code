import random
print("Infinity Dice")


ask = "yes"
def rollSides():
    sides=int(input("How many sides? :"))
    diceNumber = random.randint(0, sides)
    print("You rolled", diceNumber)
while ask== "yes":
    rollSides()
    ask=input("Roll again? ")
    