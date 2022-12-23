# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Method 1: reverse string O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = [x.lower() for x in s if x.isalnum()]
        return new == new[::-1]

#method 2: two pointer O(n), space complexity saved
class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        left, right = 0, len(s)-1

        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left, right = left+1, right-1          
        
        return True
