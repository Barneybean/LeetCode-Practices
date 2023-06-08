# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

# Example 1:

# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:

# Input: root = [1,0,48,null,null,12,49]
# Output: 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # it is a BST, so it is sorted in a way left < root < right 
        # min distance = min difference in val of the two node. 
        # in this case, must be distances between two adjancent nodes 
        
        # option 1: use in order traversal 
        prev, min_dis = None, float('inf')

        def dfs(node):
            nonlocal prev, min_dis # must call non local in recursive if using variable for tracking
            # base case 
            if not node: 
                return None 
                
            dfs(node.left) # five all the way to the most left node

            # in order is root processed in the middle of the left and right call
            if prev: # if none then move to next value
                min_dis = min(min_dis, node.val - prev.val) # node must > prev in bst in order
            prev = node # move to next node 
            
            dfs(node.right)
            
        dfs(root)
        return min_dis


        # option 2: use DFS and mimic in order

        # stack = []
        # prev = None 
        # min_dis = float('inf')

        # while stack or root: 
        #     # dig into the most left leaf of the root
        #     while root: 
        #         stack.append(root)
        #         root = root.left
            
        #     # common procedure of the stack 
        #     root = stack.pop()
        #     # min dis must be the diff in neighbors in BST
        #     if prev:
        #         min_dis = min(min_dis, root.val - prev.val)
 
        #     prev = root 
        #     # this is to go by in order taraversal, root.right become new root and go to next loop, then dig all the way to the left most leaf of it 
        #     root = root.right 
        # return min_dis









        



