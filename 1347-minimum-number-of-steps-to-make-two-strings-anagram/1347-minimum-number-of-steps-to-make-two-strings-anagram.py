class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = dict.fromkeys(string.ascii_lowercase, 0)
        
        for i in range(len(s)):
            d[s[i]] += 1
            d[t[i]] -= 1
        
        res = 0
        for v in d.values():
            if v >= 0:
                res += v
        return res