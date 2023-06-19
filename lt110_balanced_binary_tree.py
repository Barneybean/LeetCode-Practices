# Given a binary tree, determine if it is 
# height-balanced
# .

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

    # Option 1: efficient
        ans = True

        def dfs(node):
            nonlocal ans

            if not node:
                 return 0 
            
            l = dfs(node.left)
            r = dfs(node.right)
            # whenever height diff is > 1 is the same level then it is not balanced 
            if abs(l-r) > 1: 
                ans = False

            return  1 + max(l, r) # typical calculation of height, base = 0 then 1+ max(l, r)       
        dfs(root)
        return ans


    # Option 2: easy to understand but less efficient 
    #     if not root: 
    #         return True
        
    #     lh = self.height(root.left)
    #     rh = self.height(root.right)
    #     if abs(lh-rh)>1: # height differ > 1
    #         return False 
    #     # above is just 1 node: root 
    #     # need to run for each node, so cannot stop here 
    #     left = self.isBalanced(root.left) # check if left sight is balanced, it sill return true and false based on the abs(lh-rh)>1 above
    #     right = self.isBalanced(root.right)
    #     if left and right: 
    #         return True
    #     else: 
    #         return False


    # def height(self, root):
    #     if not root: 
    #         return 0 
    #     return 1 + max(self.height(root.left), self.height(root.right))