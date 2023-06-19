# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: true

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #sort arrary by start time then check if the end has overlap with the start

        if not intervals: 
            return True

        # sorted_interval = sorted(intervals, key = lambda k: (k[0], k[1]), reverse = False)
        # assume if end = next start then the person can attend
        s_int = sorted(intervals)

        end = s_int[0][1]
        for i in range(1, len(s_int)): 
            if s_int[i][0] < end: 
                return False

            # end = new meetign end
            end = s_int[i][1]
        
        return True