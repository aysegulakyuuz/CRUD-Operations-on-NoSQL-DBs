import random
import string

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

# Generate 100,000 people and save them
people_data = generate_people(100000)
