class FileSystem:

    def __init__(self):
        self.paths = defaultdict()
        

    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths or len(path) ==0 or path == "/":
            return False
        
        # rfind return the highest index val of the last occurrence of the substring from the input string
        idx = path.rfind('/')
        
        # if it is initial path, "/" can be valid as well
        if path[:idx] not in self.paths and len(path[:idx]) > 1:
            return False
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