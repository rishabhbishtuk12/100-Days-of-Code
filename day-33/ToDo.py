import os
import time
List=[]

def printList():
    print()
    for item in List:
        print(item)
    print()


Heading = "TO DO List Manager"
print(f"{Heading:^35}")
print()

while True:
    if List == []:
        item = input("What do you want to add in your to do list\n")
        List.append(item)
        
    else:
        time.sleep(1)
        os.system("clear")
        print(f"{Heading:^35}\n")
        menu = input("Do you want to view, add, or edit your to do list?\n")
        if menu == "view":
            os.system("clear")
            printList()
        elif menu == "add":
            item = input("\nWhat do you want to add?\n")
            List.append(item)
        elif menu == "edit":
            item = input("\nWhat do you want to remove?\n")
            if item in List:
                List.remove(item)
            else:
                print(f"\n{item} was not in the list")        
