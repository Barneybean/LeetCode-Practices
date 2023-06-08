# 26. Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # option 1 
        nums[:] = sorted(list(set(nums)))
        # this will ensure it is O(1)

        # two pointer
        #option 2 or use while 
        if len(nums) == 0: return 0

        pointer = 1

        for i in range(1, len(nums)):
            # if element == next element then move on, if != then move the element at i to element at pointer 
            if nums[i] != nums[i-1]:
                nums[pointer] = nums[i]
                pointer += 1 
            
        return pointer 

        # p = 1, i = 1, n[1] != n[0] 2!=1 [1,2,2,3,4]
        # p = 2, i = 2, n[2] == n[1] 2==2 [1,2,2,3,4] p no change 
        # p = 2, i = 3, n[3] != n[2] 3!=2 [1,2,3,3,4] n[2] = n[3]



