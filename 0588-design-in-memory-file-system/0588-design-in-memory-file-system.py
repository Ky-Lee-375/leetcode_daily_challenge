class FileSystem:

    def __init__(self):
        # dictionary of path
        # dictionary of files
        self.paths = collections.defaultdict(list)
        self.files = collections.defaultdict(str)
        
    def ls(self, path: str) -> List[str]:
        if path in self.files:
            return [path.split("/")[-1]]
        else:
            return self.paths[path]

    def mkdir(self, path: str) -> None:
        directories = path.split("/")
        
        for i in range(1, len(directories)):
            cur = "/".join(directories[:i]) or "/"
            if cur not in self.paths or directories[i] not in self.paths[cur]:
                bisect.insort(self.paths[cur], directories[i])

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.files:
            self.mkdir(filePath)
        self.files[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)