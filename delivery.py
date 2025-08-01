import datetime
from trucks import Truck

#Manually load packages into each truck based on task requirements and set time the truck leaves WGU
trucks = [
    Truck(1, 16, 18, None, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East", datetime.timedelta(hours=8)),
    Truck(2, 16, 18, None, [3, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=30)),
    Truck(3, 16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=0)),
]

#Define get address index from address_data
def get_address_index(address, address_data):
    for row in address_data:
        if address in row[2]:
            return int(row[0])
    raise ValueError(f"Address not found: {address}")

#Calculate distance from distance_data
def calculate_distance(index1, index2, distance_data):
    distance = distance_data[index1][index2]
    return float(distance or distance_data[index2][index1])

#Define Nearest Neighbor algorithm
def route_and_deliver(truck, package_table, address_data, distance_data):
    undelivered = [package_table.lookup(pid) for pid in truck.packages]
    truck.packages.clear()

    while undelivered:
        current_index = get_address_index(truck.address, address_data)
        nearest = min(
            undelivered,
            key=lambda p: calculate_distance(current_index, get_address_index(p.address, address_data), distance_data)
        )
        distance = calculate_distance(current_index, get_address_index(nearest.address, address_data), distance_data)

        truck.mileage += distance
        truck.time += datetime.timedelta(hours=distance / truck.speed)
        truck.address = nearest.address
        nearest.truck_number = truck.id
        nearest.departure_time = truck.departure_time
        nearest.delivery_time = truck.time
        truck.packages.append(nearest.ID)
        undelivered.remove(nearest)

#Define function to run deliveries and call Nearest Neighbor algorithm
def run_deliveries(package_table, address_data, distance_data, trucks):
    route_and_deliver(trucks[0], package_table, address_data, distance_data)
    route_and_deliver(trucks[1], package_table, address_data, distance_data)

    trucks[2].departure_time = min(trucks[0].time, trucks[1].time)
    route_and_deliver(trucks[2], package_table, address_data, distance_data)
