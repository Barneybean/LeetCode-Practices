# Given the root of a binary tree, invert the tree, and return its root.
# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#method 1: recursion
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root: 
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

#BFS
def invertTree2(self, root):
    from collections import deque #append and pop is O(1), list is O(n)
    queue = deque([(root)])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root
    
# DFS
def invertTree(self, root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.extend([node.right, node.left])
    return root
