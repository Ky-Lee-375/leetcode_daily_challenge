# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = float('-inf')
        max_path = []
        
        def dfs(node):
            nonlocal res
            if node == None:
                return 0, []
            
            left_sum, left_path = dfs(node.left)
            right_sum, right_path = dfs(node.right)
            
            left_sum = max(0, left_sum)
            right_sum = max(0, right_sum)
            
            curr_sum = node.val+left_sum+right_sum
            if curr_sum > res:
                res = curr_sum
                if left_sum > right_sum:
                    max_path = left_path + [node.val] + list(reversed(right_path))
                else:
                    max_path = right_path + [node.val] + list(reversed(left_path))
                    
            return_parent_sum = node.val + max(left_sum,right_sum)
            
            if left_sum >right_sum:
                return return_parent_sum, left_path + [node.val]
            else:
                return return_parent_sum, right_path + [node.val]
        dfs(root)
        return res