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

start_time = time.time()
with driver.session() as session:
    people = session.read_transaction(read_people)
elapsed_time = time.time() - start_time

print(f"✅ Neo4j Read Completed! Time: {elapsed_time:.5f} seconds")

driver.close()
