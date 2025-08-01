# Create class for trucks
from dataclasses import dataclass
from datetime import datetime
from typing import List, Any

#Define truck class
@dataclass
class Truck:
    id: int
    capacity: int
    speed: float
    load: int
    packages: List[Any]
    mileage: float
    address: str
    departure_time: datetime
    time: datetime = None

#Define time from depature time
    def __post_init__(self):
        self.time = self.departure_time

#Define return string from truck
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.id, self.capacity, self.speed, self.load, self.packages, self.mileage, self.address, self.departure_time)
