# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t = len(digits) - 1
        digits[t] = digits[t] + 1
        #return list if no need to carry 
        if digits[t] < 10:
            return digits
        # if least position + 1 >= 10 then carry 1 to number on the left 
        carry = 1
        while carry == 1:
            digits[t] = digits[t] % 10
            # eg: 9 + 1 = 10
            if t <= 0:
                return [1]+digits 
            t = t-1
            digits[t] = digits[t] + carry
            if digits[t] < 10:
                carry = 0
        return digits
            
