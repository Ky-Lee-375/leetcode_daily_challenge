class FileSystem:

    def __init__(self):
        self.paths = defaultdict()
        

    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths:
            return False
        
        idx = path.rfind("/")
        if path[:idx] not in self.paths and len(path[:idx]) > 1:
            return False
        self.paths[path] = value
        return True
        

    def get(self, path: str) -> int:
        return self.paths.get(path) if path in self.paths else -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)