# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#%%
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #DP i - word1, j - word2
        # replace1 -> next compare (i+1, j+1)
        # insert1 -> next compare (i, j+1)
        # delete1 -> next compare (i+1, j) 
        # word1 = "", word2 = "abc" then need 3 edits so default action of the matrix should be the number of edit needed when "" against portion of word2
        l1 = len(word1)
        l2 = len(word2)
        cache = [[float("inf") for x in range(l2+1)] for y in range(l1+1)]
        # print(cache) when word1 = 'abc', word2 = 'acbd'
        #     a.    c.    b.    d. 
        # a[[-inf, -inf, -inf, -inf, 3], 
        # b [-inf, -inf, -inf, -inf, 2], 
        # c [-inf, -inf, -inf, -inf, 1], 
        #   [ 4,    3,    2,    1,   0]]
        # bottom up 
        for a in range(l1, -1, -1):
            cache[l1-a][-1] = a
        for b in range(l2, -1, -1):
            cache[-1][l2-b] = b

        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                if word1[i] == word2[j]:
                    # no edit needed
                    cache[i][j] = cache[i+1][j+1]
                else: 
                    # 1(at least 1 edit for non matching char)+min of three edits: replace, insert, delete1
                    cache[i][j] = 1+min(cache[i+1][j+1], cache[i][j+1], cache[i+1][j])
        return int(cache[0][0])


