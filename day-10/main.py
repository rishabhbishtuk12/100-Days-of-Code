myBill = float(input("What was the bill?: "))
tip = int(input("How much tip would you like to give?: "))
numberOfPeople = int(input("How many people?: "))
finalBill = (myBill * (1 + tip / 100)) / numberOfPeople
answer = round(finalBill, 2)
print("You all owe", answer)
