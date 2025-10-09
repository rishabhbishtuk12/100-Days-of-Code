import os,time,pymongo,datetime

client = pymongo.MongoClient("mongodb+srv://rishabhbishtuk12_db_user:Fy0JWX1wwh1tvgvK@replit.6wlvs3b.mongodb.net/")
db = client["my_diary"]
collection = db["diary_data"]

def addItem():
    time.sleep(1)
    os.system("clear")
    timestamp = str(datetime.datetime.now())
    print("Diary entry for",timestamp)
    print()
    add = input("> ")
    data = {"_id": timestamp,"task":add}
    collection.insert_one(data)

def findItem():
    find = collection.find()
    for item in find:
        time.sleep(1)
        os.system("clear")
        print(item["_id"])
        print(item["task"])
        print()
        ask = input("Next or Exit: ").title()
        if ask == "Exit": 
            break

password = "AAbb"

print("My Diary\n")
userInput = input("Password: ")
if userInput != password:
    print("Incorrect")
    exit()
print("WELCOME")


while True:
    time.sleep(1)
    os.system("clear")
    print("1: Add\n2: View")
    menu =input(">")
    if menu == "1":
        addItem()
    elif menu == "2":
        findItem()
        

    else:print("\033[31m"" Wrong input..! Select 1 or 2 only""\033[0m")     

  
    # try:
    #     menu = int(input(">"))
    #     if menu == 1:
    #         date = datetime.datetime.today()
    #         print("Diary entry for",date)
    #         add = input("> ")
    #         Data = {"_id": date,"task":add}
    #         collection.insert_one(add)
    #     elif menu == 2:


    # except:print("\033[31m"" Wrong input..! Select 1 or 2 only""\033[0m")



