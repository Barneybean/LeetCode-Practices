# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: 
            return True

        seen = set()

        while n not in seen: 
            seen.add(n)
            num = 0 # for cumulative sum
            while n > 0:
                digit = n % 10
                num += digit ** 2
                n = n//10 #get to next digit
            
            if num == 1: # happy number found
                return True 

            n = num # otherwise, repeat

        return False #loop detected

            

