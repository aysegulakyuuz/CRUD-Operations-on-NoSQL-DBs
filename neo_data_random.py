import random
import string
import time
from neo4j import GraphDatabase

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

# Generate 100,000 people
people_data = generate_people(100000)

# Neo4j Connection
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"

driver = GraphDatabase.driver(uri, auth=(user, password))

# Function to insert people into Neo4j
def create_people(tx, people):
    for person in people:
        tx.run("CREATE (:Person {name: $name, age: $age, city: $city, job: $job})",
               name=person["name"], age=person["age"], city=person["city"], job=person["job"])

# Insert Data into Neo4j and Measure Time
start_time = time.time()
with driver.session() as session:
    session.write_transaction(create_people, people_data)
elapsed_time = time.time() - start_time

print(f"✅ Neo4j Insert Completed! Time: {elapsed_time:.5f} seconds")

# Close Neo4j Connection
driver.close()
