# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

# Example 1:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
# Example 2:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips: return True

        # use DP and go by stations 
        sorted_trips = sorted(trips, key = lambda x: x[2]) # sort by end for building station
        DP = [0] * (sorted_trips[-1][-1] + 1) # first station is 1, second in DP
        
        people = DP[0]

        # calculate net passenger in each start and end 
        for passenger, start, end in sorted_trips: 
            DP[start] += passenger
            DP[end] -= passenger
        
        # if the first station is overloaded then return False 
        if DP[0] > capacity:
            return False
        
        # cumulate net passengers and check against capcity 
        for i in range(1, len(DP)): # first station is 1, second in DP
            people += DP[i]
            if people > capacity: 
                return False 
        
        return True


