class UndergroundSystem:

    def __init__(self):
        self.users_data = {}
        self.average_trip = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
            self.users_data[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.users_data[id].extend([stationName, t])
        
        stations = self.users_data[id][0] + ' ' + self.users_data[id][2]
        user_trip_time = t - self.users_data[id][1]
        
        if stations in self.average_trip:
            self.average_trip[stations].append(user_trip_time)
        else:
            self.average_trip[stations] = [float(user_trip_time)]
        
        self.users_data[id] = []

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        stations = startStation + ' ' + endStation
        print(self.average_trip[stations])
        average_time = sum(self.average_trip[stations]) / len(self.average_trip[stations])
        return average_time


test = UndergroundSystem()
test.checkIn(45, 'Leyton', 3)
test.checkOut(45, 'Waterloo', 15)
print(test.users_data)
print(test.average_trip)
print(test.getAverageTime('Leyton', 'Waterloo'))
