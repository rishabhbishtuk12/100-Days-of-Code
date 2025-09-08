import time,os

def color(a):
    if a == "r":
        print("\033[31m", end="")
    elif a == "g":
        print("\033[32m", end="")
    elif a == "y":
        print("\033[33m", end="")
    elif a == "b":
        print("\033[34m", end="")
    elif a == "p":
        print("\033[35m", end="")
    elif a == " ":
        print("\033[0m", end="")

ask = input("What sentence do you want rainbow-ising?")
for a in ask:
    color(a.lower())
    print(a,end="")
print()