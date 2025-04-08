import time
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb+srv://admin:1234@nosql-test.n23d8.mongodb.net/?retryWrites=true&w=majority")
db = client["NoSQL_Test"]
collection = db["People"]

# Read Operation
start_time = time.time()
people = list(collection.find({}))  # Retrieve all records
elapsed_time = time.time() - start_time

print(f"✅ MongoDB Read Completed! Time: {elapsed_time:.5f} seconds")
