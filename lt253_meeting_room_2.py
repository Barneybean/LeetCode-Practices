# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # key is to break the start and end time into separate list 

        if not intervals:
            return 0

        start = sorted([m[0]for m in intervals])
        end = sorted([m[1] for m in intervals])

        #start = [0, 5, 15, 20, 35]
        #end =   [10, 20, 30, 40, 50]
        
        room = 0
        # use two pointers 
        s, e = 0, 0
       
        # option 1:
        # use while loop when using 2 pointer so you can stop the first pointer
        # while s < len(start):
        #     if start[s] >= end[e]: 
        #         e += 1 # check next meeting end
        #     else:
        #         room += 1
        #     s += 1 # move to next meeting start
            
        # option 2:
        max_room = 0
        while s < len(start):
            if start[s] < end[e]:
                room += 1 
                s += 1 
            else:
                room -= 1 # a meeting ends
                e += 1 # check next meeting end
            max_room = max(room, max_room)

        return max_room 


        # --------------------------
        #    -------       ------------
        #        -------
        
        # [[13,15],[1,13],[6,9]]
        #         ----
        # --------
        #     --


        