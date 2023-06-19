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
        max_room = 0
        # use two pointers 
        s, e = 0, 0

        #Option 1
        while s < len(start):
            if start[s] < end[e]: # start is before current end 
                room += 1
                s += 1 # only increment start here 
            elif start[s] > end[e]: # new meeting start after cur meeting end 
                e += 1 # end current meeting 
                room -= 1 # no change becuase end one start another 
            else: # faster if split out == case 
                s += 1
                e += 1
                # if end and start at the same time, then no change in room 
            max_room = max(max_room, room)

        return max_room


        # Option 2
        # while s < len(start):
        #     if start[s] < end[e]:
        #         room += 1 
        #         s += 1 
        #     else:
        #         room -= 1 # a meeting ends
        #         e += 1 # check next meeting end
        #     max_room = max(room, max_room)

        # return max_room 


        # --------------------------
        #    -------       ------------
        #        -------
        
        # [[13,15],[1,13],[6,9]]
        #         ----
        # --------
        #     --


        