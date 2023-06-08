# Given two strings s and t, return the number of distinct 
# subsequences
#  of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

 

# Example 1:

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
# Example 2:

# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # it is very similar to Longest Sub Arrary 
        # t must be visited so then hitting boundary of t then return 1 as match found


        ## EXAMPLE : s = "abbt" t = "abt"	##
		## STACK TRACE ##
        #       j  0  1  2
        # [        a  b  t  
        #      i 
        #    0 a  [1, 0, 0, 0], 
        #    1 b  [1, 0, 0, 0], 
        #    2 b  [1, 0, 0, 0], 
        #    3 t  [1, 0, 0, 0], 
        #         [1, 0, 0, 0], 
        # ]
        
		## TIME COMPLEXITY : O(MxN) ##
		## SPACE COMPLEXITY : O(MxN) ##
        
        ##### Option 1: DP
        n = len(s) # y axis
        m = len(t) # x axis 
        if n < m: 
            return 0

        memo = [[0]*(m+1) for _ in range(n+1)]

        for row in memo:
            row[0] = 1
        #i is y axis, number of rows, index of s 
        for i in range(1, len(memo)): # start with 1 then check from i-1. no for len+1
            for j in range(1, len(memo[0])): # len(memo[0]) or m + 1
                # only increment when matches multiple 
                memo[i][j] = memo[i-1][j] 
                if s[i-1] == t[j-1]: # start from i-1 = 0
                    memo[i][j] = memo[i-1][j] + memo[i-1][j-1]
                
        return memo[-1][-1]


        ###### Option 2 swap s to x axis and t to y axis
        # len_s = len(s)
        # len_t = len(t)

        # memo = [[0]*(len_s+1) for _ in range(len_t+1)]

        # memo[0] = [1]*(len_s+1)

        # for i in range(1, len(memo)):
        #     for j in range(1, len(memo[0])):
        #         memo[i][j] = memo[i][j-1]
        #         if s[j-1] == t[i-1]:
        #             memo[i][j] = memo[i-1][j-1] + memo[i][j-1]
        
        # return memo[-1][-1]

        # Option 3 Recursion with Memo
        ## EXAMPLE : s = "abbt" t = "abt"	##
		## STACK TRACE ##
        #       j  0  1  2
        # [        a  b  t  
        #    i 
        #    0 a  [1, 0, 0, 0], 
        #    1 b  [1, 0, 0, 0], 
        #    2 b  [1, 0, 0, 0], 
        #    3 t  [1, 0, 0, 0], 
        #         [1, 0, 0, 0], 
        # ]


        ####### Option 3: recursion with memo
        # to find count of string use 1+rec
        # here it is finding number of words so set base number on the extra space
        # when using recursion starting from m-1 and n-1, it will match from beginiing letters
        ## STACK TRACE ##
        #       j     0  1  2
        # [           a  b  t  
        #    i    [1, 0, 0, 0, 0],
        #    0 a  [1, 0, 0, 0, 0], 
        #    1 b  [1, 0, 0, 0, 0], 
        #    2 b  [1, 0, 0, 0, 0], 
        #    3 t  [1, 0, 0, 0, 0], 
        #         [1, 0, 0, 0, 0], 
        # ]
        # len_s = len(s)  # y axis
        # len_t = len(t)  # x axis
        # memo = [[0] * (len_t + 1) for _ in range(len_s + 1)]

        # def recur(i, j, memo):
        #     # base cases, run until exhausted s => i==0
        #     if i < 0 and j >= 0: #first row and -1 row
        #         return 0
        #     if j < 0:  # s ended but not able to match all t, first column and to the left 
        #         return 1
            
        #     # recursion case, usually if else statement
        #     if memo[i][j] != 0:
        #         return memo[i][j] # calculated

        #     if s[i] == t[j]:
        #         memo[i][j] = recur(i - 1, j - 1, memo) + recur(i - 1, j, memo)
        #     else: 
        #         memo[i][j] = recur(i - 1, j, memo)
        #     return memo[i][j]

        # return recur(len_s-1, len_t-1, memo) # 4,3,memo


        # Option 4 recursive with cache
        # from functools import cache
        # @cache
        # def solve(i, j):
        #     if j == len(t):
        #         return 1
        #     if i == len(s):
        #         return 0
        #     ans = solve(i + 1, j)
        #     if s[i] == t[j]:
        #         ans += solve(i + 1, j + 1)
        #     return ans
        # return solve(0, 0)
        