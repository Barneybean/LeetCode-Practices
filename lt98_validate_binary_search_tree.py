# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(root, low, high):
            if not root:
                return True
            elif not (low < root.val and root.val < high):
                return False
            left =  traverse(root.left,    low,    root.val) 
            right = traverse(root.right, root.val, high)
            return left and right 
        
        return traverse(root,low=float('-inf'), high=float('inf'))