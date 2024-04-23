class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # edge case:
            # len(s) != len(t)
        # create dictionary for each character
        d = dict.fromkeys(string.ascii_lowercase, 0)
        # iterate through s and t
        # increment for t
        # decrement for s
        for i in range(len(s)):
            d[s[i]] -= 1
            d[t[i]] += 1
        answer = 0
        
        for k in d.values():
            answer += max(0, k)
        return answer