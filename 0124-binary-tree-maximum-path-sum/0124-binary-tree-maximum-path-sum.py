# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")
        if root is None:
            return -1001
        
        def recurse_max(node):
            nonlocal max_path
            if node is None:
                return 0
            left_sum = max(recurse_max(node.left), 0)
            right_sum = max(recurse_max(node.right), 0)
            
            current = node.val + left_sum + right_sum
            max_path = max(max_path, current)
            return node.val + max(left_sum, right_sum)
        
        recurse_max(root)
        return max_path
        