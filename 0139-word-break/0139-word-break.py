class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        counter = [0]
        for i in range(len(s)):
            for j in counter:
                if s[j:i+1] in wordDict:
                    counter.append(i+1)
                    break
        return counter[-1] == len(s)
                
        