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
        # use two pointers
        # save the longest, second longest
        best = 0
        
        # dfs on every child of the node
        # compare w max1 and 2 
        # update accordingly
        def dfs(node):
            if node == 0:
                return 0
            nonlocal best
            max1, max2 = 0,0
            
            for child in node.children:
                depth = dfs(child)
                # add +1 to include the current node
                depth += 1
                if depth > max1:
                    max1, max2 = depth, max1
                elif depth > max2:
                    max2 = depth
                
            best = max(best, max1+max2)
        # keep track of best
        # compare w taking max1 and max2
        
            return max1
        # return the longest
        
        # call dfs on root
        # return the best
        dfs(root)
        return best