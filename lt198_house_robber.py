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
        class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []: return 0
        
        #option 1
        max_rob1, max_rob2 = 0, 0 #add two houses before the list 

        # example [rob1=0, rob2=0, n, n+1, n+2]
        # at position n, the best it can get is the max of rob1+n or just rob2

        for n in nums:
            max_rob_at_n = max(max_rob1 + n, max_rob2)
            # max at n+2 = max(max_rob at n, max_rob at n+1) so move the two pointer down
            max_rob1 = max_rob2
            max_rob2 = max_rob_at_n
        
        return max_rob2 # or max_rob_at_n

        # option 2 use DP
        # draw a brute force way
        # nums = [1, 2, 3, 1, 4, 5]
        # two type of starts: 
        # rob 1: then nums[0] + rob[0+2:n]
        # rob 2: then nums[1] + rob[1+2:n]

        # then it becomes DP problem 
        # in rob 1: rob[0+2:n] has same two possible solutions until the end 
        # so rob = max((num[0] + rob[0+2: n]), (num[1]+rob[3:n]))

        # at the end, we are comparing whether the rob1 and rob2 start
        
        if nums == []: return 0
        # nums =[1,2,3,1]
        # dp = [0,1,0,0,0], calculate the max from 1st and 2nd house
        dp = [0]* (len(nums)+1)
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i+1] = max(dp[i], (dp[i-1] + nums[i])) # {max_rob at i (dp[i])} or {max_rob at i-1 + current house value}
            print(i, dp)
        return dp[-1]



