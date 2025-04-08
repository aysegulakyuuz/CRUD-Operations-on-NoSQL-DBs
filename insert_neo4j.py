import time
from neo4j import GraphDatabase
from generate_data import people_data

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
