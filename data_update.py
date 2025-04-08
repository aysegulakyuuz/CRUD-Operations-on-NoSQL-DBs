import time
from pymongo import MongoClient

# MongoDB Bağlantısı
client = MongoClient("mongodb+srv://admin:1234@nosql-test.n23d8.mongodb.net/?retryWrites=true&w=majority")
db = client["NoSQL_Test"]
collection = db["People"]

# Update Operation (Change job titles)
start_time = time.time()

# "Software Engineer" olanları "Senior Software Engineer" yap
collection.update_many({"job": "Software Engineer"}, {"$set": {"job": "Senior Software Engineer"}})


collection.update_many({"age": {"$lt": 30}}, {"$set": {"job": "Junior Developer"}})

elapsed_time = time.time() - start_time

print(f"✅ MongoDB Update Completed! Time: {elapsed_time:.5f} seconds")
