# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # edge case
        if root is None:
            return float('-inf')
        
        res = float('-inf')
        max_path = []

        def dfs(node):
            nonlocal res, max_path
            if node is None:
                return 0, []
            
            left_sum, left_path = dfs(node.left)
            right_sum, right_path = dfs(node.right)

            # Use max to discard negative paths
            left_sum = max(0, left_sum)
            right_sum = max(0, right_sum)
            
            # Calculate current sum through this node
            current_sum = node.val + left_sum + right_sum
            if current_sum > res:
                res = current_sum
                # Reconstruct the path leading to this maximum
                if left_sum > right_sum:
                    max_path = left_path + [node.val] + list(reversed(right_path))
                else:
                    max_path = right_path + [node.val] + list(reversed(left_path))

            # Return the max sum and path to parent
            return_to_parent_sum = node.val + max(left_sum, right_sum)
            if left_sum > right_sum:
                return return_to_parent_sum, left_path + [node.val]
            else:
                return return_to_parent_sum, right_path + [node.val]
        
        dfs(root)
        print("Maximum path sum is:", res)
        print("Path for maximum sum:", max_path)
        return res    
        
        # clarifying questions
        # can root be empty
        # can it have negative value
        # binary tree
        
# print logest path

        