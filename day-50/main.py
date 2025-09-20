import os,time,random

def add():
    os.system("clear")
    print("IDEAS\n")
    f = open("idea.list","a+")
    idea = input("Idea > ")
    f.write(f"{idea}\n")
    f.close()

def load():
    os.system("clear")
    print("IDEAS\n")
    f = open("idea.list","r")
    ideas = f.read().split("\n")
    f.close()
    ideas.remove("")
    idea = random.choice(ideas)
    print(idea)
    time.sleep(2)

while True:
    os.system("clear")
    print("IDEAS\n")
    print("Press 1: ADD an idea")
    print("Press 2: Load up a random idea\n")
    

    menu = int(input("> "))
    time.sleep(1)
    if menu == 1:
       add()
    elif menu == 2:
        load()
    else:
        print("Invalid INPUT ")