import time
from neo4j import GraphDatabase

# Neo4j Connection
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"

driver = GraphDatabase.driver(uri, auth=(user, password))

def update_jobs(tx):
    # "Software Engineer" olanları "Senior Software Engineer" yap
    tx.run("MATCH (p:Person) WHERE p.job = 'Software Engineer' SET p.job = 'Senior Software Engineer'")
    # Yaşı 30'dan küçük olanları "Junior Developer" yap
    tx.run("MATCH (p:Person) WHERE p.age < 30 SET p.job = 'Junior Developer'")

start_time = time.time()
with driver.session() as session:
    session.execute_write(update_jobs)
elapsed_time = time.time() - start_time

print(f"✅ Neo4j Update Completed! Time: {elapsed_time:.5f} seconds")

driver.close()
