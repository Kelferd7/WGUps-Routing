from dataclasses import dataclass
import datetime

@dataclass
class Package:
    ID: int
    address: str
    city: str
    state: str
    zipcode: str
    deadline: str
    weight: str
    note: str = ""
    status: str = "At Hub"
    departure_time: datetime.timedelta = None
    delivery_time: datetime.timedelta = None
    truck_number: int = None
    corrected_address: str = None
    correction_time: datetime.timedelta = None

    def __str__(self):
        delivery_time_str = self.delivery_time if self.delivery_time else "N/A"
        return (f"Package {self.ID} | Address: {self.address} | Deadline: {self.deadline} | "
                f"Truck: {self.truck_number} | Status: {self.status} | Delivery Time: {delivery_time_str}")

    def update_status(self, convert_timedelta):
    #Handle packages that are delayed
        if self.note and "delayed" in self.note.lower():
            if convert_timedelta < datetime.timedelta(hours=9, minutes=5):
                self.status = "Delayed"
                return
    #Handle package 9 for wrong address
        if self.ID == 9:
            correction_time = datetime.timedelta(hours=10, minutes=20)
            if convert_timedelta < correction_time:    
                self.address = "300 State St"
                self.status = "At Hub"
                return
            else:
                self.address = "410 S State St., Salt Lake City, UT 84111"

        if self.delivery_time and convert_timedelta >= self.delivery_time:
            self.status = "Delivered"
        elif self.departure_time and self.departure_time <= convert_timedelta < self.delivery_time:
            self.status = "En route"
        else:
            self.status = "At Hub"
