class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if s1 == s2:
            return True
        
        swap = []
        for i in range(n):
            if s1[i] != s2[i]:
                swap.append((s1[i], s2[i]))
        if len(swap) < 2:
            return False
        return len(swap) == 2 and swap[0][0] == swap[1][1] and swap[0][1] == swap[1][0]
        