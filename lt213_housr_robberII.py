# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:

# Input: nums = [1,2,3]
# Output: 3

class Solution:
    def rob(self, nums: List[int]) -> int:
        # since the first and last house are adjacent so use the house robber twice
        # if start with first then the nums = nums[:-1] to exclude the last house
        # if start with second then the nums = nums[1:]
        # then take the max of two
        if nums == []: return 0
        def house_rob(arr):
            # put max value in dp2 every turn, compare 1+new with 2 and add max of these two in 3, then roll forward
            dp1, dp2 = 0, 0 
            for n in arr: 
                temp = dp1
                dp1 = dp2
                dp2 = max(dp2, temp+n) 
            return dp2 

        return max(house_rob(nums[1:]), (nums[0]+house_rob(nums[2:-1])))
        # starting from 2 becuase it needs 2 previous house nums[0] and nums[0] needs to be robbed no matter how in second scenario
