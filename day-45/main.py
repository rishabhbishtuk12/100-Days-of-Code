import time,os
toDoList=[]
def add():
    time.sleep(1)
    os.system("clear")
    print("Add\n")
    name = input("What is it?")
    date = input("When it is due")
    priority = input("How Important?")
    row = [name,date,priority]
    toDoList.append(row)

def view():
    time.sleep(1)
    os.system("clear")
    print("View\n")
    print("1: View All\n2: View Priority")
    viewMenu = input("> ")
    if viewMenu == "1":
      for row in toDoList:
        for i in row:
            print(i, end=" | ")
        print()
      print()
      time.sleep(1)
    elif viewMenu == "2":
        priority = input("Which Priority")
        for row in toDoList:
            if priority in row:
                for i in row:
                    print(i, end=" | ")
                print()
        time.sleep(1)
def remove():
    time.sleep(1)
    os.system("clear")
    name = input("What would you like to remove? ")
    for row in toDoList:
        if name in row:
          toDoList.remove(row)

def edit():
    time.sleep(1)
    os.system("clear")
    find = input("What do you want to edit? ")
    for row in toDoList:
      if find in row:
        toDoList.remove(row)
        name = input("What is it?")
        date = input("When it is due")
        priority = input("How Important?")
        newRow = [name,date,priority]
        toDoList.append(newRow)
        return
    else:
       print("item not found")

print(toDoList)
while True:
  print("ToDO List Mangement System\n")
  print("1: Add\n2: View\n3: Remove\n4: Edit")
  print()
  menu=input("> ")
  if menu == "1":  
    add()
  elif menu =="2":
    view()    
  elif menu =="3":
    remove() 
  elif menu =="4":
    edit()
  time.sleep(1)
  os.system("clear")
