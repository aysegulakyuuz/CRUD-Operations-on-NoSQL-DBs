import time
from neo4j import GraphDatabase

# Neo4j Connection
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"

driver = GraphDatabase.driver(uri, auth=(user, password))

# Function to read people from Neo4j
def read_people(tx):
    result = tx.run("MATCH (p:Person) RETURN p.name, p.age, p.city, p.job")
    return [record for record in result]

# Start measuring time
start_time = time.time()

with driver.session() as session:
    people = session.read_transaction(read_people)

# Measure elapsed time
elapsed_time = time.time() - start_time

# Output the results
print(f"✅ Neo4j Read Completed! Time: {elapsed_time:.5f} seconds")

# Optionally print the first 5 people to verify the results
print("\nFirst 5 records:")
for person in people[:5]:  # Print the first 5 records
    print(person)

# Close Neo4j Connection
driver.close()
