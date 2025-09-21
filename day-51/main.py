import os,time
heading="TO DO LIST"
doList=[]

f = open("toDo.list","r")
doList = eval(f.read())
f.close()

def viewList():
    print(f"{heading:^35}")
    count = 1
    for i in doList:
        print(f"{count}: {i}")
        count+=1

while True:
    print(f"{heading:^35}")
    menu = input("\nDo you want to view, add, edit, remove or delete an item from the to do list?\n").title()
    if menu == "View":
        viewList()

    elif menu == "Add":
        item = input("\nWhat do you want to add:\n").title()
        doList.append(item)

    elif menu == "Remove":
        item = input("\nWhat do you want to remove:\n").title()
        sure = input("\nAre you sure you want to remove it\n").title()
        if sure == "Yes":
            doList.remove(item)   

    elif menu == "Edit":
        item=input("\nWhat do you want to edit to remove ?\n").title()
        newItem = input("\nWhat do you want to change it to?\n").title()
        for i in range (0,len(doList)):

            if doList[i]==item:
                doList[i]=newItem

    elif menu == "Delete":
        doList=[]
    f = open("toDo.list", "w")
    f.write(str(doList))
    f.close()

    time.sleep(2)
    os.system("clear")        

