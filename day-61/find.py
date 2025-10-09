import pymongo

uri = "mongodb+srv://rishabhbishtuk12_db_user:Fy0JWX1wwh1tvgvK@replit.6wlvs3b.mongodb.net/"
client = pymongo.MongoClient(uri)

db = client["Rishabh"]
collection = db['mySampleCollection']

# allDb = client.list_database_names()
# print(allDb)

# col = client["Rishabh"]
# print(col.list_collection_names())

# many = collection.find({"name":"Yashu"},{"_id":0})
# for item in many:
#     print(item)

# pve = {"name": "Yashu"}
# nextt = {"$set":{"marks":10}}
# ub = collection.update_many(pve,nextt)
# print(ub.modified_count)

# rec = {"name":"Yashu"}
# collection.delete_many(rec)

allDoc = collection.find({"name":"rishabh", "marks":{"$lte":50}},{"_id":0})
for item in allDoc:
    print(item)