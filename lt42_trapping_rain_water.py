# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

class Solution:
    def trap(self, height: List[int]) -> int:

        # formula: min(max(left), max(right)) of i minus height[i] => how much water can trap at 1 location 
        # use left, right pointer 
        if not height: return False 

        # two pointers
        left, right = 0,len(height)-1
        # to hold max of left and right 
        max_left, max_right = height[0], height[-1]
        res = 0

        # calculate from lower of left, right max, because the lower of two is what the next position can hold 
        while left < right:
            if max_left < max_right:
                # 0 position cannot hold water, so check right 
                left += 1 
                add = max_left - height[left]
                if add < 0: 
                    add = 0 
                res += add
                # update max_left 
                max_left = max(max_left, height[left])
            else: 
                ritrght -= 1 
                add = max_right - height[right]
                if add < 0: 
                    add = 0 
                res += add
                # update max_right
                max_right = max(max_right, height[right])
        
        return res 

        # brute force 
        # input    [4,2,0,3,2,5]
        # maxleft  [4,4,4,4,4,5]
        # max_right[5,5,5,5,5,5]
        # min().   [4,4,4,4,4,5]
        #water=min() - input
        #.         [0,2,4,1,2,0] = 9




