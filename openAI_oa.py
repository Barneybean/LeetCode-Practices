# questions: return nth positive number that is a multiple of a list of numbers
# for example: n = 4, multipliers = [3, 5]
#     then return 9 becuase the mutiplier = [3,5,6,9,10]

#%%
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'nth_multiplier' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY multipliers
#

def nth_multiplier(n, multipliers):
    # Write your code here
    # use heap to improve efficiency 
    from heapq import heapify, heappop, heappush
    h = [] # initialize a min heap with positive number
    res = None
    count = 1 

    while count <= n*n:
        for e in multipliers:
            heappush(h, e*count)
        count += 1
    
    for x in range(n-1): # heap is not sorted, but h[0] is garanteed to be the smallest
        print(heappop(h))

    print(h) #[9, 10, 12, 15, 18*, 15*, 24, 20, 30, 25, 36, 30, 21, 35, 48, 40, 27, 45, 75, 50, 33, 55, 80, 60, 39, 65, 42, 70, 45]

        
    return h[0]
    

if __name__ == '__main__':
    
    print(nth_multiplier(4, [3,5]))

# %%
# testing heapq
def test(nums):
    from heapq import heapify, heappush, heappop
    # minheap like a queue
    min_heap = []
    for n in nums: 
        heappush(min_heap, n)
    # print('after push', min_heap)
    # after push [3, 5, 6, 10, 9, 15, 12, 20] not ordered 
    
    # for x in range(1): # heap is not sorted, but h[0] is garanteed to be the smallest
        # print(heappop(min_heap)) # 3 
        # [5, 9, 6, 10, 20, 15, 12]
    
    heappop(min_heap)
    
    
    print(min_heap)
    
test([3, 5, 6, 10, 9, 15, 12, 20])


# %%
from heapq import heapify, heappush, heappop
nums = [4,1,3,4,5]
h = []

for n in nums:
    heappush(h, n)

print(h)

# %%
