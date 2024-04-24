class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None
        
class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = capacity
        
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev =self.right, self.left
    
    def remove(self, node):
        pr, nxt = node.prev, node.next
        pr.next = nxt
        nxt.prev = pr
        
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        put_node = Node(key, value)
        self.cache[key] = put_node
        self.insert(put_node)
        
        if len(self.cache) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# clarifying question
# if value is put to already existing key
# doens't output anything?

# algorithm
# doubly linked list
# class Node
# lru on the left, most recent on the right