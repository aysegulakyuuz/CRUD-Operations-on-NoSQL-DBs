import time
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb+srv://admin:1234@nosql-test.n23d8.mongodb.net/?retryWrites=true&w=majority")
db = client["NoSQL_Test"]
collection = db["People"]

# Delete Operation (Remove all records)
start_time = time.time()
collection.delete_many({})
elapsed_time = time.time() - start_time

print(f"✅ MongoDB Delete Completed! Time: {elapsed_time:.5f} seconds")
