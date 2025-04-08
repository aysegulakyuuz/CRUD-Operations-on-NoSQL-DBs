import time
from pymongo import MongoClient
from data.generate_data import people_data

# MongoDB 
client = MongoClient("mongodb+srv://admin:1234@nosql-test.n23d8.mongodb.net/?retryWrites=true&w=majority")
db = client["NoSQL_Test"]
collection = db["People"]


start_time = time.time()
collection.insert_many(people_data)
elapsed_time = time.time() - start_time

print(f"✅ MongoDB Insert Completed! Time: {elapsed_time:.5f} seconds")


