class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # create a dict w all letter
        d = dict.fromkeys(string.ascii_lowercase, 0)
        
        # increment for s
        # decrement for t
        for i in range(len(s)):
            d[s[i]] += 1
            d[t[i]] -= 1
        
        # go through the dict
        # sum the positive
        res = 0
        for k in d.keys():
            res += max(0, d[k])
        return res
        