import random
import string
import time
from pymongo import MongoClient

# Predefined lists of cities and jobs
cities = ["New York", "Los Angeles", "London", "Berlin", "Tokyo", "Paris", "Toronto", "Sydney", "Dubai", "Singapore"]
jobs = ["Engineer", "Doctor", "Teacher", "Lawyer", "Nurse", "Police Officer", "Software Developer", "Driver", "Designer", "Accountant"]

# Function to generate random people
def generate_people(num):
    people = []
    for _ in range(num):
        name = ''.join(random.choices(string.ascii_letters, k=10))  # Random 10-letter name
        age = random.randint(18, 80)  # Random age between 18 and 80
        city = random.choice(cities)  # Random city
        job = random.choice(jobs)  # Random job
        people.append({"name": name, "age": age, "city": city, "job": job})
    return people

# MongoDB Connection
client = MongoClient("mongodb+srv://admin:1234@nosql-test.n23d8.mongodb.net/?retryWrites=true&w=majority")
db = client["NoSQL_Test"]
collection = db["People"]

# Generate 100,000 people
people_data = generate_people(100000)

# Insert Data and Measure Time
start_time = time.time()
collection.insert_many(people_data)
elapsed_time = time.time() - start_time

print(f"✅ MongoDB Insert Completed! Time: {elapsed_time:.5f} seconds")
