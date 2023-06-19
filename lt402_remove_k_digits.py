# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # idea is to use stack to hold new strings 
        # need make smaller number on the left and maintain current order 

        stack = [] 
        res = ''

        for n in num: 
            # k > 0, still need to remove numbers 
            # remove number at the end of stack if new number to add is smaller 
            while stack and k > 0 and stack[-1] > n:
                stack.pop() # remove the number for lower number to append
                k -= 1 # remove number up to k 
        
            stack.append(n)

        # if after while loop, there is still k > 0, take the [:-k]
        if k > 0: 
            res = stack[:-k]
        else: 
            res = stack 
        
        # print(res)
        # strip leading 0 
        ##### Cannot pop in for loop, the list is not changing in forloop after popping
        while res and res[0] == '0': 
            res.pop(0)

        if res == []: return '0'

        return ''.join(res)