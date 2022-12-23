# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        l = len(s)
        if l <= 1:
            return l

        odd = 0
        f = {}
        res = []
        for e in set(s):
            f[e] = s.count(e) 
        
        # add nearst smaller even numbers to result
        for x in f.values():
            res.append(x)
            if x % 2 != 0: 
                odd += 1
        
        # if odd count exist, plus 1 
        if odd > 0:
            return sum(res)-odd+1
            
        return sum(res)