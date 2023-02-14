# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:

# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There is no odd numbers in the array.

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        odd_cnt = 0 
        sub_cnt = 0 # keep current sub count that is nice 
        nice_cnt = 0

        for i in range(len(nums)): # i is right pointer
            if nums[i]%2 == 1: 
                odd_cnt += 1
                sub_cnt = 0 #only reset when new odd in right

            # for every right, find different left that creates a nice sub
            while odd_cnt == k: 
                sub_cnt += 1 
                # reduce odd number if left is odd 
                if nums[left]%2 ==1:
                    odd_cnt -= 1 
                # then increment left 
                left += 1 

            nice_cnt += sub_cnt
        
        return nice_cnt
