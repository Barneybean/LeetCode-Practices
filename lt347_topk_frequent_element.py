# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use heap, O(1) read
        # first create a count of each unique element 
        d = {}
        for n in nums:
            if n in d:
                d[n]+=1
            else:
                d[n]=1
        
        from heapq import heappop, heappush
        h = [] # initialize heap, default min heap
        for key in d: 
            # heap will sort by first value in tupple 
            heappush(h, (d[key], key)) # o(log(k))
            if len(h) > k:
                heappop(h)
            
        res = []
        while h:
            cnt, ele = heappop(h) # Pop and return the smallest item from the heap
            res.append(ele)
        
        return res # might need to reverse the order 

            