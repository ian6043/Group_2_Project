import csv
import networkx as nx
from itertools import product


# Function to read csv and store variables and clauses
def read_sat_csv(file_path):
    variables = set()
    clauses = []

    with open(file_path, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            clause = [int(x) for x in row]  # Convert each value to an integer
            clauses.append(clause)

            # Add absolute values of variables to the set
            for var in clause:
                variables.add(abs(var))

    return variables, clauses


v, c = read_sat_csv("test1.csv")

print(v)
print(c)
