class Trie:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = True

    def search(self, word: str) -> bool:
        node = self.findPrefix(word)
        if node is not None and '$' in node:
            return node
        return None
        
    def findPrefix(self, prefix):
        node = self.root
        for c in prefix:            
            if c not in node: return None
            node = node[c]
        return node
    
    def startsWith(self, prefix: str) -> bool:
        return self.findPrefix(prefix) is not None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)