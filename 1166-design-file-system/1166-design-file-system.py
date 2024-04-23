class FileSystem:

    def __init__(self):
        self.paths = defaultdict()
        

    def createPath(self, path: str, value: int) -> bool:
        # check if path already exists
        if not path or not value or path in self.paths:
            return False
        # if so, return false
        
        dash_idx = path.rfind('/')
        # find the last occurence of /
        # if everything before doesn't exist-> return false
        if path[:dash_idx] not in self.paths and len(path[:dash_idx]) > 1:
            return False
        # if exists, add the new item
        self.paths[path] = value
        return True
        

    def get(self, path: str) -> int:
        if path in self.paths:
            return self.paths[path]
        else:
            return -1
        
        
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

# Clarifying questions
# "/" can be valid if it is the first path
# single string and val to store