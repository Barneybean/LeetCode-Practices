# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        if len(nums)<3:
            return []
        
        z,p,n = [], [], []
        #use set for positive and negetive because no duplicate triplets in result

        # allocate all numbers in to zpn
        for e in nums: 
            if e == 0:
                z.append(e)
            if e > 0:
                p.append(e)
            if e < 0:
                n.append(e)
                
        N,P = set(n), set(p)

        # when there is 0 in nums
        if len(z) >= 3:
            res.add(tuple([0,0,0])) # set cannot add list but tuple is ok to add

        if z: 
            for x in n: 
                if -1*x in P:
                    res.add(tuple(sorted([x, 0, -x])))
        
        # when there is no 0:
            #a. sum two number in N (Negative) and find its inverse in P (positive)
        for i in range(len(n)-1):
            for j in range(i+1,len(n)):
                s = -1*(n[i] + n[j])
                if (s in P):
                    res.add(tuple(sorted([n[i], n[j], s])))
            #b. sum two number in P and find its inverse in N 

        for i in range(len(p)-1):
            for j in range(i+1,len(p)):
                
                s = -1*(p[i]+p[j])
                if s in N:
                    res.add(tuple(sorted([p[i], p[j], s])))
        
        return list(res)
            

#Brute Force, Not recommended 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums)<3:
            return []
        res = []
        for i in range(len(nums)-2): 
            for j in range(i+1,len(nums)-1):
                t = nums[i] + nums[j]
                remain = nums[j+1:]
                comb = sorted([nums[i], nums[j], t*(-1)])
                if (t*(-1) in remain) and (comb not in res):
                    res.append(comb)
        return res
