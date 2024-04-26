# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # base case
        # when root is none -> return -inf
        if root == None:
            return float('-inf')
        
        # consider the negative values
        res = float('-inf')
        # recursively find the max
        def dfs_max(node):
            nonlocal res
            # base case
            if node == None:
                return 0
            # get the right tree
            # compare with 0?
            right = max(0, dfs_max(node.right))
            left = max(0, dfs_max(node.left))
            
            curr = node.val + right + left
            res = max(res, curr)
            return node.val + max(right, left)
        dfs_max(root)
        return res