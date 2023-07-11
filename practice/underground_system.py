"""
The problem with the UndergroundSystem class is to design a system that keeps track of customer travel times between different stations in an underground railway system. The system needs to provide functionality to check-in customers at a station, check them out at another station, and calculate the average travel time between any two stations based on the recorded data.

To solve this problem, we can use two main data structures:
1. Dictionary to store the check-in information of customers: We can use a dictionary to store the check-in details of each customer using their unique ID. The key-value pairs in the dictionary would be ID -> (start station, start time).

2. Dictionary to store the total travel time and count for each start and end station pair: We can use another dictionary to store the total travel time and count for each pair of start station and end station. The key-value pairs in this dictionary would be (start station, end station) -> [total travel time, count].

The solution involves the following steps:

1. Initialize the data structures: Create the two dictionaries mentioned above.

2. Check-in: When a customer checks in, store their check-in details in the first dictionary using their ID as the key.

3. Check-out: When a customer checks out, retrieve their check-in details using their ID from the first dictionary. Calculate the travel time by subtracting the check-in time from the check-out time. Update the total travel time and count for the corresponding start and end station pair in the second dictionary.

4. Get average travel time: To calculate the average travel time between two stations, retrieve the total travel time and count for the given start and end station pair from the second dictionary. Divide the total travel time by the count to get the average travel time.

This approach allows us to efficiently keep track of the travel times between stations and calculate the average travel time when needed.
"""

# from collections import defaultdict

# class UndergroundSystem:
#     def __init__(self):
#         # Stores the check-in details for each customer
#         self.check_ins = {}

#         # Stores the total travel time and count for each start and end station pair
#         self.travel_times = defaultdict(lambda: [0, 0])

#     def checkIn(self, id: int, stationName: str, t: int) -> None:
#         # Record the check-in details for the customer
#         self.check_ins[id] = (stationName, t)

#     def checkOut(self, id: int, stationName: str, t: int) -> None:
#         # Retrieve the check-in details for the customer
#         start_station, start_time = self.check_ins[id]

#         # Calculate the travel time
#         travel_time = t - start_time

#         # Update the total travel time and count for the start and end station pair
#         self.travel_times[(start_station, stationName)][0] += travel_time
#         self.travel_times[(start_station, stationName)][1] += 1

#         # Remove the check-in details for the customer
#         del self.check_ins[id]

#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         # Retrieve the total travel time and count for the start and end station pair
#         total_time, count = self.travel_times[(startStation, endStation)]

#         # Calculate the average travel time
#         average_time = total_time / count

#         return average_time

# undergroundSystem = UndergroundSystem()

# undergroundSystem.checkIn(45, "Leyton", 3)
# undergroundSystem.checkIn(32, "Paradise", 8)
# undergroundSystem.checkIn(27, "Leyton", 10)
# undergroundSystem.checkOut(45, "Waterloo", 15)
# undergroundSystem.checkOut(27, "Waterloo", 20)
# undergroundSystem.checkOut(32, "Cambridge", 22)

# average1 = undergroundSystem.getAverageTime("Paradise", "Cambridge")
# average2 = undergroundSystem.getAverageTime("Leyton", "Waterloo")

# undergroundSystem.checkIn(10, "Leyton", 24)

# average3 = undergroundSystem.getAverageTime("Leyton", "Waterloo")

# undergroundSystem.checkOut(10, "Waterloo", 38)

# average4 = undergroundSystem.getAverageTime("Leyton", "Waterloo")

# print("Average time (Paradise to Cambridge):", average1)  # Output: 14.0
# print("Average time (Leyton to Waterloo):", average2)  # Output: 11.0
# print("Average time (Leyton to Waterloo) after additional check-in:", average3)  # Output: 11.0
# print("Average time (Leyton to Waterloo) after check-out:", average4)  # Output: 12.0



class UndergroundSystem:
    def __init__(self):
        # Stores the check-in details for each customer
        self.check_ins = {}

        # Stores the total travel time and count for each start and end station pair
        self.travel_times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # Record the check-in details for the customer
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Retrieve the check-in details for the customer
        start_station, start_time = self.check_ins[id]

        # Calculate the travel time
        travel_time = t - start_time

        # Update the total travel time and count for the start and end station pair
        key = (start_station, stationName)
        if key in self.travel_times:
            self.travel_times[key][0] += travel_time
            self.travel_times[key][1] += 1
        else:
            self.travel_times[key] = [travel_time, 1]

        # Remove the check-in details for the customer
        del self.check_ins[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # Retrieve the total travel time and count for the start and end station pair
        key = (startStation, endStation)
        total_time, count = self.travel_times[key]

        # Calculate the average travel time
        average_time = total_time / count

        return average_time


undergroundSystem = UndergroundSystem()

undergroundSystem.checkIn(None, None, None)
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)

average1 = undergroundSystem.getAverageTime("Paradise", "Cambridge")
average2 = undergroundSystem.getAverageTime("Leyton", "Waterloo")

undergroundSystem.checkIn(10, "Leyton", 24)

average3 = undergroundSystem.getAverageTime("Leyton", "Waterloo")

undergroundSystem.checkOut(10, "Waterloo", 38)

average4 = undergroundSystem.getAverageTime("Leyton", "Waterloo")

print("Average time (Paradise to Cambridge):", average1)  # Output: 14.0
print("Average time (Leyton to Waterloo):", average2)  # Output: 11.0
print("Average time (Leyton to Waterloo) after additional check-in:", average3)  # Output: 11.0
print("Average time (Leyton to Waterloo) after check-out:", average4)  # Output: 12.0