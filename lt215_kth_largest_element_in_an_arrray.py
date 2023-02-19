# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# You must solve it in O(n) time complexity.

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minheap
        min_heap = []
        for n in nums: 
            heappush(min_heap, n)
            # start to pop after K numbers in min_heap
            if len(min_heap)>k:
                # heappop will remove the largest 
                heappop(min_heap)
        return min_heap[0]

        # maxheap
        # python has only minheap so implement max heap using -x
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap) # remember this usage
        print(max_heap)
        for n in nums[:k-1]:
            heappop(max_heap)
        return -max_heap[0] # need reverse




