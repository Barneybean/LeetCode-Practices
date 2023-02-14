# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.


# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"

# Intuition
# mimic human calculation from the least significant digit

# Approach
# Complexity
# Time complexity:
# O(N)
# Space complexity:
# O(1)
# Code
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0 
        res = ""
        l1 = len(num1)
        l2 = len(num2)
        if l1>l2:
            num2 = (l1-l2)*"0"+num2
        elif l1<l2:
            num1 = (l2-l1)*"0"+num1
        
        for i in range(len(num1)-1,-1,-1):
            
            sum = int(num1[i]) + int(num2[i]) + carry
            res = str(sum%10) + res

            if sum >= 10: 
                carry = 1 
            else: 
                carry = 0
        
        if carry == 1: 
            res = '1'+res
            
        return res
            
            