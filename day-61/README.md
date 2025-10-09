# 🗃️ MongoDB with Python (PyMongo)

This project demonstrates how to connect and interact with **MongoDB** using **Python’s PyMongo library**.  
It includes examples of creating databases, inserting, reading, updating, and deleting documents — the essential CRUD operations.

---

## 📚 What I Learned

- 🔌 How to **connect Python with MongoDB** using the `pymongo` library
- 🏗️ How to **create databases and collections** in MongoDB
- 🧩 How to **insert single and multiple documents**
- 🔍 How to **find and filter data** using `find()` and query operators
- ✏️ How to **update and delete documents**
- ⚙️ How to **integrate MongoDB operations** into Python applications

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install pymongo
```

### 2. Connect to MongoDB

You can connect either to a local MongoDB server or MongoDB Atlas (cloud).

```py
from pymongo import MongoClient

# For local MongoDB

client = MongoClient("mongodb://localhost:27017/")

# For MongoDB Atlas

# client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/")
```

### 🧮 Basic CRUD Operations

➕ Insert Documents

```py
db = client["mydatabase"]
collection = db["students"]

# Insert one document

collection.insert_one({"name": "Rishabh", "age": 22})

# Insert many documents

collection.insert_many([
{"name": "John", "age": 25},
{"name": "Emma", "age": 23}
])
```

### 🔍 Read Documents

```py
for doc in collection.find():
print(doc)

# Filtered query

for doc in collection.find({"age": {"$gt": 21}}):
print(doc)
```

### ✏️ Update Documents

```py
collection.update_one({"name": "Rishabh"}, {"$set": {"age": 23}})
```

### ❌ Delete Documents

```py
collection.delete_one({"name": "John"})
```

### 💾 Example Output

```py
Connected to MongoDB successfully!

{'\_id': ObjectId('...'), 'name': 'Rishabh', 'age': 22}
Data inserted and displayed successfully.
```

### 🧠 Key Takeaways

- PyMongo makes MongoDB integration simple and Pythonic
- MongoDB stores data as flexible JSON-like documents
- CRUD operations are lightweight and scalable
- Ideal for data-driven applications and APIs

### 🧰 Tech Stack

- Python 3
- MongoDB / MongoDB Atlas
- PyMongo
