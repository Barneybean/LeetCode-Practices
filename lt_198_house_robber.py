# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.


class Solution:
    def rob(self, nums: List[int]) -> int:
        #4liner
        dp1, dp2 = 0, 0
        for n in nums:
            dp1, dp2 = dp2, max(dp2, dp1+n)
        return dp2


        #use DP
        # if nums == []: return 0
        # # nums =[1,2,3,1]
        # # dp = [0,1,0,0,0], calculate the max from 1st and 2nd house
        # dp = [0]* (len(nums)+1)
        # dp[1] = nums[0]
        # for i in range(1, len(nums)):
        #     dp[i+1] = max(dp[i], (dp[i-1] + nums[i]))
        #     print(i, dp)
        # return dp[-1]

#      [1, 2, 3, 1, 2, 100]

# 1 [0, 1, 2, 0, 0, 0, 0]
# 2 [0, 1, 2, 4, 0, 0, 0]
# 3 [0, 1, 2, 4, 4, 0, 0]
# 4 [0, 1, 2, 4, 4, 6, 0]
# 5 [0, 1, 2, 4, 4, 6, 104]
