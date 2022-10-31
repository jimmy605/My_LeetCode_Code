class Solution:
    """
    - Atleast one trip
    - Each trip has 3 integers
    - Atleast 1 passenger
    - 0 <= from
    - Capacity is atleast 1
    
    ['num_passengers', 'from', 'to'], capacity = passengers
    """
    def __init__(self):
        self.trips_data = {}
    
    def check_car_pooling(self, capacity):
        for num_passengers in self.trips_data.values():
            if num_passengers > capacity:
                return False
        return True 
    
    def carPooling(self, trips, capacity):
        for trip in trips:
            num_passengers, start, stop = trip 
            for location in range(start, stop):
                if location not in self.trips_data:
                    self.trips_data[location] = num_passengers
                else:
                    self.trips_data[location] += num_passengers
            
            if self.check_car_pooling(capacity) == False:
                return False 
        
        return True 


testing = Solution()
print(testing.carPooling([[2,1,5],[3,3,7]], 4))

testing_2 = Solution()
print(testing_2.carPooling([[4,1,3],[3,3,7]], 4))