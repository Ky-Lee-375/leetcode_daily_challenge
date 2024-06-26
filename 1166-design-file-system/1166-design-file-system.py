class FileSystem:

    def __init__(self):
        #path
        self.paths = collections.defaultdict()
        

    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths:
            return False
        
        # rfind: returns highest idx value of last occurrence
        idx = path.rfind('/')
        
        # if parent path doesnt exist -> return false
        if path[:idx] not in self.paths and len(path[:idx]) >1:
            return False
        self.paths[path] = value
        return True
        

    def get(self, path: str) -> int:
        return self.paths.get(path) if path in self.paths else -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)