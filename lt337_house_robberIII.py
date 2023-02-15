# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

# Example 1:


# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:


# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # use dfs, recursion, return [rob_root, not_rob_root]
        def dfs(root):
            # base case 
            if not root:
                return [0,0]
            
            left_tree = dfs(root.left)
            right_tree = dfs(root.right)

            # value from robbing root, skip root of next so use [1]
            rob_root = root.val + left_tree[1] + right_tree[1]
            # if root is not robbed, then I can robb skips, no restrictions, therefore I would take the max from left and max from right 
            not_rob_root = max(left_tree) + max(right_tree)

            return [rob_root, not_rob_root]

        return max(dfs(root))
