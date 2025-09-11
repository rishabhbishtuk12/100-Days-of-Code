# myDictionary = {"name": "Ian", "health":219,"strength":199,"equipped":"Axe"}

# for j, i in myDictionary.items():
#     print(f"{j}: {i}")
#     if(j=="strength"):
#         if (i>100):
#             print("Whoa, So Strong!")
#         else:
#             print("Weak Sauce Dude!")
import os,time
myDictionary = {"name":None,"url":None,"desc":None,"rating":None}
    
for name in myDictionary.keys():
    os.system("clear")
    myDictionary[name]=input(f"{name}: ")
    time.sleep(1)

print()
os.system("clear")
for name,value in myDictionary.items():
    print(f"{name}: {value}")