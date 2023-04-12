# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validateHelper(root, left, right):
            if root is None:
                return True
            rootV = root.val
            if rootV <= left or rootV >= right:
                return False
            return validateHelper(root.left, left, rootV) and validateHelper(root.right, rootV, right)
        return validateHelper(root, float("-inf"), float("inf"))
        
        