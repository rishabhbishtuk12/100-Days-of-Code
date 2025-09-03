import os
import time

myAgenda = []

def printList():
    print()
    for item in myAgenda:
        print(item)
    time.sleep(1)
    print()

while True:
    os.system('clear')
    menu = input("Add or Remove?: ")
    if menu == "add":
        item = input("What's next on the Agenda?: ")
        myAgenda.append(item)
    elif menu == "remove":
        item = input("What's do you want to remove?: ")
        if item in myAgenda:
            myAgenda.remove(item)
        else:
            print(f"{item} was not present in the list")


    printList()