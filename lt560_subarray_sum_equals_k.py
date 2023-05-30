# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # method1: using hashmap O(n)
        # idea:  if sum[i]−sum[j]=k, the sum of elements lying between indices i and j is k.
        if nums == []:
            return 0

        h = {0:1} # if cum sum = k then count as 1 [1, 3] k = 3, then 3 - 3 = 0 
        sum = 0
        target = 0 
        res = 0 
        
        for n in nums: 
            sum += n 
            target = sum - k 
            
            if target in h: 
                res += h[target] # add all possible result from previous
        # ie [1,2,3] -> res = 2, then [1,2,3, 1, -1], same sum so res += 2 because 1+-1=0
            if sum in h:
                h[sum] += 1 # cum sum count + 1
            else: 
                h[sum] = 1 # new cum sum count = 1

            # this if else is equivalend to h[sum] += h.get(sum, 0) + 1 
        return res

        # X method 2: using prefix sum O(n2)
        # idea: two pointers, difference = k then it is satisfied
        # sum = [0] * (len(nums) + 1)
        # count = 0 
        # # calculate cumulative sum 
        # for i in range(1,len(sum)): 
        #     sum[i] = sum[i-1]+nums[i-1]
        # print(sum)
        # for start in range(len(sum)):
        #     for end in range(start+1, len(sum)):
        #         if sum[end]-sum[start] == k: 
        #             count += 1
        # return count 
