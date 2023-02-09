# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # https://youtu.be/lXVy6YWFcRM 
        # -2*-3 can be the largest so we keep track of the min and max each time new number is multiplied 
        # initialize
        res = max(nums)
        cur_min, cur_max = 1, 1 
        for n in nums: 
            if n == 0: 
                cur_min, cur_max = 1, 1 
                continue 
            
            temp = cur_max * n 
            cur_max = max(cur_max*n, cur_min*n, n)
            cur_min = min(temp, cur_min*n, n) # in case of - * - becomes larger
            # as the product might be reset so refresh the res with largest as it show up
            res = max(res, cur_max) 


        return res 

