## Chunk 67

**Original Text:**

Implementing the DRT service and imposing a toll of 0.20 EUR/km on car
users yields a significant reduction in car usage and a more dominant mode shift effect from car to DRT. As shown
in Fig. 2d and 3d, more than a third of all DRT users come from the car mode. The car trip share in the Berlin area
decreases by approx. 12% (minimum DRT fee: 3 EUR), and PT, bicycle, walk and DRT trip shares increase.

---

**LLM Contextual Output:**

Here's an example implementation in Python:

```python
class TripData:
    def __init__(self):
        self.car_trips = []
        self.pt_trips = []
        self.pt_only_trips = []

    def add_car_trip(self, distance_km, time_taken):
        trip = {
            'distance_km': distance_km,
            'time_taken': time_taken
        }
        self.car_trips.append(trip)

    def calculate_toll(self, car_trips):
        total_distance_km = sum(distance for distance, _ in car_trips)
        toll_amount = 0.20 * total_distance_km
        return toll_amount

    def add_pt_trip(self, distance_km, time_taken):
        trip = {
            'distance_km': distance_km,
            'time_taken': time_taken
        }
        self.pt_trips.append(trip)

    def calculate_trip_shares(self):
        car_share = len([trip for trip in self.car_trips if trip['distance_km'] > 0]) / len(self.car_trips)
        pt_only_share = sum(1 for trip in self.pt_only_trips if trip['distance_km'] <= 0) / len(self.pt_only_trips)
        pt_share = (len([trip for trip in self.pt_trips if trip['distance_km'] > 0]) + 
                    len([trip for trip in self.pt_only_trips if trip['distance_km'] <= 0])) / len(self.pt_trips)

        print("Car Trip Share:", car_share)
        print("PT Only Trip Share:", pt_only_share)
        print("PT Trip Share:", pt_share)


# Example usage:
dt = TripData()

dt.add_car_trip(100, 30)  # 1 km trip
dt.add_car_trip(200, 45)  # 2 km trip

dt.add_pt_trip(10, 15)   # 1 km trip
dt.add_pt_trip(20, 25)   # 3 km trip

toll_amount = dt.calculate_toll(dt.car_trips)
print("Toll Amount:", toll_amount)

dt.add_pt_trip(5, 8)     # 2 km trip (PT only)
dt.add_pt_trip(15, 18)  # 4 km trip
dt.add_pt_trip(30, 35)  # 6 km trip

dt.calculate_trip_shares()
```

This implementation defines a `TripData` class to store car trips and PT trips. The `add_car_trip`, `add_pt_trip`, and `calculate_toll` methods allow you to add data to the object. The `calculate_trip_shares` method calculates the share of each mode of transport.

In the example usage, three car trips are added with a distance of 100 km and two PT trips with distances of 10 km and 20 km. A toll amount is then calculated using the `calculate_toll` method, which multiplies the total distance by the toll rate. The `add_pt_trip` methods are used to add more PT trips, including one trip that only uses the pedestrian or bike path. Finally, the `calculate_trip_shares` method prints out the share of each mode of transport for both car and PT trips.
