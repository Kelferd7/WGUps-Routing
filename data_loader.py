import csv
from hashtable import HashMap
from packages import Package

#Define function to load from CSV file
def load_csv(file_path):
    with open(file_path) as file:
        return list(csv.reader(file))

#Define function to load packages to hash table from CSV files
def load_packages(file_path):
    hash_table = HashMap()
    with open(file_path) as file:
        reader = csv.reader(file)
        for row in reader:
            pkg = Package(
                int(row[0]), row[1], row[2], row[3],
                row[4], row[5], row[6], row[7]
            )
            hash_table.insert(pkg.ID, pkg)
    return hash_table

#Define function to load each CSV file to a specific variable
def load_all_data():
    distance_data = load_csv("distances.csv")
    address_data = load_csv("addresses.csv")
    package_table = load_packages("packages.csv")
    return package_table, address_data, distance_data
