# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None or subRoot == None:
            return False
        
        def traverseCheck(r,s):
            if not s and not r:
                return True
            if not s or not r:
                return False
            if r.val == s.val and traverseCheck(r.left, s.left) and traverseCheck(r.right, s.right):
                return True
            else:
                return False
        if traverseCheck(root,subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        return False