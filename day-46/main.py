# clue = {}
# def prettyPrint():
#     print()
#     for key, value in clue.items():
#         print(key, end=": ")
#         for subkey, subvalue in value.items():
#             print(subkey, subvalue, end=" | ")
#         print()

# while True:
#     name = input("Name: ")
#     location = input("Location: ")
#     weapon = input("Weapon: ")
#     clue[name] = {"location": location, "weapon": weapon}
#     prettyPrint()


import os,time

mokeDex = {}
def pretyPrint():
  print(f"Name\tType\tHP")
  for key,value in mokeDex.items():
    # print(f"{value} | ",end='')
      print(f"""{key:^5}|{value["type"]:^8}|{value["hp"]:^4}""")
      
while True:
  time.sleep(1)
  os.system("clear")
  print("\nMokeBeasts Full-on MokeDex\n")
  print("Add your Beast!")
  name = input("Name > ")
  type = input("Type > ")
  hp = input("HP > ")
  mokeDex[name]={"type":type,"hp":hp}
  print("----------")
  print()
  pretyPrint()
  