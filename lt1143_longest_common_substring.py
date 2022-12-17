# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

#method 1: Recursion with Memoization O(?)
class Solution:        
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
    
        m = len(s1)
        n = len(s2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.helper(s1, s2, 0, 0, memo)

    def helper(self, s1, s2, i, j, memo):
        if memo[i][j] < 0:
            if i == len(s1) or j == len(s2):
                memo[i][j] = 0
            elif s1[i] == s2[j]:
                memo[i][j] = 1 + self.helper(s1, s2, i + 1, j + 1, memo)
            else:
                memo[i][j] = max(
                    self.helper(s1, s2, i + 1, j, memo),
                    self.helper(s1, s2, i, j + 1, memo),
                )
        return memo[i][j]


text1 = "abcde"
text2 = "ace"
s = Solution()
s.longestCommonSubsequence(text1, text2)
#%%
m = 5
n = 3
print([[-1 for _ in range(n + 1)] for _ in range(m + 1)])

# %%
# method 2: Recursion witout memoization O(mn),
class Solution: 
    def longestCommonSubsequence(self, s1: str, s2: str) -> int: 
        #1. lcs(i, j): i j is the index of each letter in text1 and text2
            # base case: if text1 reaches end or text2 reaches end: return 0 
            # elif text1[i] == text2[j] then return 1+LCS(i+1, j+1)
            # return max(lcs(i+1), lcs(j+1))
        return self.recursion(text1, text2, 0, 0)
    
    def recursion(self, text1, text2, i=0, j=0):
        if (i == len(text1)) or ((j == len(text2))):
            return 0    
        elif text1[i] == text2[j]:
            return 1+self.recursion(text1, text2, i+1, j+1)
        else:
            return max(
                self.recursion(text1, text2, i+1,j), 
                self.recursion(text1, text2, i,j+1)
                )