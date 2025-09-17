import os,time,random
trumps = {}
trumps["Mr Spock"] = {"Intelligence": 150, "Speed": 100, "Guile": 50, "Baldness Level": 25}
trumps["David"] = {"Intelligence": 100, "Speed": 50, "Guile": 25, "Baldness Level": 150}
trumps["Monica from Friends"] = {"Intelligence": 50, "Speed": 25, "Guile": 150, "Baldness Level": 100}
trumps["Professor X"] = {"Intelligence": 25, "Speed": 150, "Guile": 100, "Baldness Level": 50}


while True:
    os.system("clear")
    print('TOP TRUMPS')
    print('----------')
    print()
    print('Characters \n')
    for key in trumps:
        print(key)
    userChar = input("\n Pick your Character : ").title()
    computerChar = random.choice(list(trumps.keys()))
    print("\nComputer has Picked", computerChar )
    Stat = input("Choose your Stat: Intelligence, Speed, Guile & Baldness Level: ").title()

    print()
    print(f"{userChar}: {trumps[userChar][Stat]}")
    print(f"{computerChar}: {trumps[computerChar][Stat]}")
    print()

    if trumps[userChar][Stat] > trumps[computerChar][Stat]:
        print(f"************* {userChar}, Win! *************")
    elif trumps[userChar][Stat] < trumps[computerChar][Stat]:
        print(f"************* {computerChar}, Win! *************")
    else:
        print("************* Draw! *************")

    time.sleep(3)