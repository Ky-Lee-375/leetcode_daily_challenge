class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # at most one swap 
        if s1 == s2:
            return True
        n = len(s1)
        stack = []
        
        # loop through s1 
        # add to stack if diff
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                stack.append((s1[i], s2[i]))
                
        # if stack size is 2 true else false
        if len(stack) != 2:
            return False
        return stack[0][0] == stack[1][1] and stack[0][1] == stack[1][0]