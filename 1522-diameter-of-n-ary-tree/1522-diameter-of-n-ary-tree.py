"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        best = 0
        def dfs(node):
            if node == None:
                return 0
            max1 = 0
            max2 = 0
            for child in node.children:
                nonlocal best
                depth = dfs(child)
                depth += 1
                if depth > max1:
                    max1, max2 = depth, max1
                elif depth > max2:
                    max2 = depth
            best = max(best, max1+max2)
            return max1
        dfs(root)
        return best
                
        
        # call dfs on root