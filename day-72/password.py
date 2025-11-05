import pymongo

password = "AA1"
salt = 11
#newPassword = f'{password}{salt}'
newPassword = hash(password)
print(newPassword)

#client = pymongo.MongoClient("mongodb+srv://rishabhbishtuk12_db_user:Fy0JWX1wwh1tvgvK@replit.6wlvs3b.mongodb.net/")
#db = client["my_diary"]
#collection = db['user_info']
#collection.insert_one({"password": newPassword})


