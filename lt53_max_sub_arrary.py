# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

#DP
        # dp = [0 for x in nums]
        # dp[0] = nums[0]
        # # each position holds the max value of sub arrarys starting from this pos
        # for i in range(1,len(nums)):
        #     dp[i] = max(dp[i-1]+nums[i], nums[i])
        # # dp:  [-2,1,-2,4,3, 5,6, 1,5] save the max in dp then add next 
        # # number in nums, if new number is larger then nums[i] then keep, 
        # # else start with new num
        # # nums:[-2,1,-3,4,-1,2,1,-5,4]
        # return max(dp)
         
# pointer Fastest O(n)
        max_sub = nums[0]
        cur_sum = 0 
        # cumulate sum, if cum_sum < 0 then start with 0, when cum_sum is higher than max_sub then use this number as max 
        for n in nums:
            if cur_sum < 0: 
                cur_sum = 0 
            cur_sum += n 
            max_sub = max(max_sub, cur_sum)

        return max_sub


# X brute force 
        # max_num = -math.inf
        # for i in range(len(nums)):
        #     cur_max = 0
        #     for j in range(i,len(nums)):
        #         cur_max += nums[j]
        #         max_num = max(max_num, cur_max)
        # return int(max_num)
        