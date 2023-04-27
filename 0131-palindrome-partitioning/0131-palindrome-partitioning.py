class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.helper(res, [], s)
        return res

        
    def helper(self, res, curr, s):
        if s == "":
            res.append(curr)

        for i in range(len(s)):
            if self.ispalindrome(s[:i + 1]):  
                self.helper(res, curr + [s[:i + 1]], s[i + 1:])
    
    def ispalindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True