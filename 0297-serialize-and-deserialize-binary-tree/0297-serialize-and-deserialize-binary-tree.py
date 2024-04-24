# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree = []
        def dfs(node):
        # creates a list of str
            if not node:
                tree.append("N")
                return
            # convert int to str
            tree.append(str(node.val))
            # append to the list in order
            dfs(node.left)
            dfs(node.right)
            return tree
        dfs(root)
        return ",".join(tree)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # from a comma separated list to tree
        # split
        nodes = data.split(',')
        self.i = 0
        
        def dfs():
        # iterate through the list
        # dfs
            if nodes[self.i] == "N":
                self.i += 1
                return None
        # is none -> return none
            node = TreeNode(int(nodes[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        root = dfs()
        return root
        # add left first then right

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# DFS Preorder
# left -> right