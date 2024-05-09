class FileSystem:

    def __init__(self):
        # path dict
        self.paths = collections.defaultdict()
        

    def createPath(self, path: str, value: int) -> bool:
        # if already exists -> false
        if path in self.paths:
            return False

        # see if parent path exists
        # if not -> false
        idx = path.rfind('/')
        if path[:idx] not in self.paths and len(path[:idx]) > 1:
            return False
        
        # create one
        # return true
        self.paths[path] = value
        return True        

    def get(self, path: str) -> int:
        # get path if in path dict
        return self.paths.get(path) if path in self.paths else -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)


# clarifying Q
# all lowercase?
