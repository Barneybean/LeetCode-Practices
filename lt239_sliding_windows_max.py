"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use queue to form decresing queue so extracting largest is O(1)
        q = collections.deque()
        res = []
        l = r = 0
        # loops through all numbers in nums 
        while r < len(nums):
            # remove index of smaller number than number going to add
            while q and nums[q[-1]]<nums[r]:
                q.pop() 
            # append this new number index and ensure q is desc 
            q.append(r)

            #edge case [1,-1] k = 1
            if l > q[0]:
                q.popleft()
            
            # slide the window and add idx to result after len(window)=k
            if r-l+1>=k:
                # append largest to res
                res.append(nums[q[0]])
                # slide 
                l += 1

            r=r+1

        return res
