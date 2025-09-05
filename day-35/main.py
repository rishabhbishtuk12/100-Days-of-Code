import os,time
heading="TO DO LIST"
doList=[]

def viewList():
    print(f"{heading:^35}")
    count = 1
    for i in doList:
        print(f"{count}: {i}")
        count+=1

while True:
    print(f"{heading:^35}")
    menu = input("\nDo you want to view, add, edit, remove or delete an item from the to do list?\n")
    if menu == "view":
        viewList()

    elif menu == "add":
        item = input("\nWhat do you want to add:\n")
        doList.append(item)

    elif menu == "remove":
        item = input("\nWhat do you want to remove:\n")
        sure = input("\nAre you sure you want to remove it\n")
        if sure == "yes":
            doList.remove(item)   

    elif menu == "edit":
        item=input("\nWhat do you want to edit to remove ?\n")
        newItem = input("\nWhat do you want to change it to?\n")
        for i in range (0,len(doList)):

            if doList[i]==item:
                doList[i]=newItem

    elif menu == "delete":
        doList=[]

    time.sleep(1)
    os.system("clear")        

