#011840112
#Kelley Buhlig WGUPS Routing Program C950

from data_loader import load_all_data
from delivery import run_deliveries, trucks
from cli import start_cli

#Main function to load data into applicable tables
#Call deliveries
#Call CLI for feedback to user
def main():
    package_table, address_data, distance_data = load_all_data()
    run_deliveries(package_table, address_data, distance_data, trucks)
    start_cli(package_table, trucks)

#Call main()
if __name__ == "__main__":
    main()
