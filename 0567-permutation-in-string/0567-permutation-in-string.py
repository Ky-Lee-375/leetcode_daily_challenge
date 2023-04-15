class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1= len(s1)
        lens2= len(s2)
        if lens1> lens2:
            return False
        
        l1 = [0]*26
        l2 = [0]*26
        
        for x in s1:
            l1[ord(x) - ord('a')] += 1
        
        for i in range(lens2):
            l2[ord(s2[i]) - ord('a')] += 1
            if i >= lens1:
                l2[ord(s2[i-lens1]) - ord('a')] -= 1
            if l1 == l2:
                return True
        return False