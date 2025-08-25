import random
print("Infinity Dice")

sides=int(input("How many sides? :"))
ask = "yes"
def rollSides():
    diceNumber = random.randint(0, sides)
    print("You rolled", diceNumber)
while ask== "yes":
    rollSides()
    ask=input("Roll again? ")
    