pokeyDictionary = {"Best Name": None,"Type": None,"Special Move": None,"HP": None,"MP": None}


for name in pokeyDictionary.keys():
    pokeyDictionary[name] = input(F"{name}:\t").strip().title()

if pokeyDictionary["Type"]== "Fire":
    print("\033[31m", end="")
elif pokeyDictionary["Type"]== "Water":
    print("\033[34m", end="")
elif pokeyDictionary["Type"]== "Air":
    print("\033[37m", end="")
elif pokeyDictionary["Type"]== "Earth":
    print("\033[32m", end="")
else:
    print("\033[33m", end="")

for name, value in pokeyDictionary.items():
    print(f"{name:<15}: {value}")