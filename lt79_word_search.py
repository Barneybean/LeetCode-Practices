# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


# Example 1:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set()

        # r = row, c = col, i = index in world 
        def dfs(r, c, i):
            # base case: always start with true bottom up, then if all false from all directions then stop and return false 
            if i == len(word):
                return True
            
            # base case: false if word not match or out of bound, or word end or already in path
            if (r<0 or 
                c<0 or 
                r>=row or 
                c>=col or
                board[r][c] != word[i] or 
                (r,c) in path
                ):
                return False 

            # add visited
            path.add((r, c))

            # check neighbors, if any of them return true then continue, think about starting from last node for dfs 
            res = ( 
                dfs(r+1, c, i+1) or 
                dfs(r, c+1, i+1) or 
                dfs(r-1, c, i+1) or 
                dfs(r, c-1, i+1) 
            )   
            #remove from path after visit
            path.remove((r, c))
            return res
        
        # for each starting point, run dfs
        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0): 
                    return True
        
        return False
