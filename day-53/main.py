import time,os

inv = []
try:
    f= open("inventory.list","r")
    inv = eval(f.read())
    f.close()
except:
    print("List does not exist! ")

def add():
    os.system("clear")
    print("INVENTORY")
    print("==========\n")
    item = input("Item to add > ").capitalize()
    inv.append(item)
    print("Added")
    

def view():
    os.system("clear")
    print("INVENTORY")
    print("==========\n")
    name = []
    for row in inv:
        if row not in name:
            print(f"{row} : {inv.count(row)}")
            name.append(row)
    time.sleep(1)

def remove():
    os.system("clear")
    print("INVENTORY")
    print("==========\n")
    rem = input("Item to remove > ").capitalize()
    for row in inv:
        if rem == row:
            inv.remove(rem)
            print("Removed")
        else:
            print("Item not present")


while True:
    os.system("clear")
    print("INVENTORY")
    print("==========\n")
    print("1: Add\n2: View\n3: Remove")
    user = input("> ")
    if user == "1":
        add()
    elif user == "2":
        view()
    elif user == "3":
        remove()
    else:
        print("Incorrect input!! ")
    f = open("inventory.list","w")
    f.write(str(inv))
    f.close()
    time.sleep(1)