import pymongo

uri = "mongodb+srv://rishabhbishtuk12_db_user:Fy0JWX1wwh1tvgvK@replit.6wlvs3b.mongodb.net/"
client = pymongo.MongoClient(uri)

db = client["Rishabh"]
collection = db['mySampleCollection']

dictonary = [
    {"name": "rishabh", "marks": 23},
    {"name": "Pari", "marks": 99},
    {"name": "Yashu", "marks": 23},
    {"name": "Yashu", "marks": 3}
    
    ]
collection.insert_many(dictonary)