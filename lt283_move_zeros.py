# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # snowball
        ball = 0
        for i in range(len(nums)):
            if nums[i] == 0: 
                ball += 1 
            else:
                nums[i-ball], nums[i] = nums[i], nums[i-ball]
        
        return nums 