import os,time

orderList = []

try:
    f = open("order.list", "r")
    orderList = eval(f.read())
    f.close()
except:
    print("Error: List file Not Found")

def add():
    time.sleep(1)
    os.system("clear")
    name = input("Name: ").title()
    toppings = input("Toppings: ").title()
    size = input("Size (S/L/M): ").capitalize()
    cost = 0
    if size == "S":
         cost = 99.4
    elif size == "M":
        cost = 149.4
    elif size == "L":
        cost = 199.4
    else:
        cost = 199.4
    while True:
        try:
            quantity = int(input("Quantity: "))
            break
        except:
            print("Invalid Quantity, Give Quantity in integer")
    prize = round((cost*quantity),2)
    row = [name,toppings,size,quantity,prize]
    orderList.append(row)
        

def view():
    h1 = "Name"
    h2 = "Topping"
    h3 = "Size"
    h4 = "Quantity"
    h5 = "Total"
    print(f"{h1:^10}{h2:^20}{h3:^10}{h4:^10}{h5:^10}")
    for row in orderList:
        print(f"{row[0]:^10}{row[1]:^20}{row[2]:^10}{row[3]:^10}{row[4]:^10}")

while True:
    time.sleep(2)
    os.system("clear")
    print("Romio Pizza")
    print(f"1: Pizza Name\n2: View Pizza")
    menu = input("> ")
    if menu == "1":
        add()
    elif menu == "2":
        view()
    else:
        print("Invalid Input Press 1 or 2")   
    f = open("order.list", "w")
    f.write(str(orderList))
    f.close()    

