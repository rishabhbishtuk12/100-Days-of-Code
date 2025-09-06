# name = input("what is my name? ")
# if name.lower().strip() == "rishabh":
#     print("hello rishabh")
# else:
#     print("who are you")

# myList = []

# def printList():
#     print()
#     for i in myList:
#         print(i)
#     print()

# while True:
#     addItem = input("Item > ").strip().capitalize()
#     if addItem not in myList:
#         myList.append(addItem)
#     printList()

# whatToEat = input("What do you fancy for dinner? ").strip().lower()
# if whatToEat == "pasta": 
#   print("Get out the pasta maker.")
# elif whatToEat == "tacos":
#   print("Let's do Taco Tuesday!")
# else: 
#   print("Go search the fridge.")

nameList = []
def printList():
    print()
    for i in nameList:
        print(i)
    print()

while True:
    firstName = input("First Name: ").strip().capitalize()
    lastName = input("Last Name: ").strip().capitalize()
    finalName = (f"{firstName} {lastName}")
    if finalName not in nameList:
        nameList.append(finalName)
        printList()
    else:
        print("\nError: Duplicate Name ")
    
