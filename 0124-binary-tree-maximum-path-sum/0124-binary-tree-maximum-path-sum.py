# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return float("-inf")
        
        res =  float("-inf")
        # dfs
        def dfs(node):
            nonlocal res
            if node == None:
                return 0
        # compare right and left
            right = max(0, dfs(node.right))
            left = max(0, dfs(node.left))
            res = max(res, node.val+right+left)
            
            # keep the larger one
            return node.val + max(left, right)
        # return the val of current node
        dfs(root)
        return res
        