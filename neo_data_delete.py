import time
from neo4j import GraphDatabase

# Neo4j Connection
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"

driver = GraphDatabase.driver(uri, auth=(user, password))

# Function to delete all Person nodes
def delete_people(tx):
    tx.run("MATCH (p:Person) DETACH DELETE p")

# Measure time for the delete operation
start_time = time.time()
with driver.session() as session:
    session.execute_write(delete_people)
elapsed_time = time.time() - start_time

print(f"✅ Neo4j Delete Completed! Time: {elapsed_time:.5f} seconds")

# Close Neo4j Connection
driver.close()
