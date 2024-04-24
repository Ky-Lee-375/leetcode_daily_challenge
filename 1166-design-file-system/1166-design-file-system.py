class FileSystem:

    def __init__(self):
        self.paths = defaultdict()
        

    def createPath(self, path: str, value: int) -> bool:
        # check if it already exists
        if path in self.paths:
        # if so, return false
            return False
        
        idx = path.rfind("/")
        # find the up until last /
        parent = path[:idx]
        if parent not in self.paths and len(parent) > 1:
        # if that X exist in path and it's greater than 1
            return False
        # return false
        
        # otherwise, add a new path
        self.paths[path] = value
        return True


    def get(self, path: str) -> int:
        return self.paths[path] if path in self.paths else -1
        

        
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

# Clarifying questions
# "/" can be valid if it is the first path
# single string and val to store