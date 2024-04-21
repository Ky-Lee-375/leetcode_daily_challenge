class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        stack = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                stack.append((s1[i], s2[i]))
        if len(stack) > 2 or len(stack) == 1:
            return False
        if len(stack) == 0:
            return True
        return (stack[0][1] == stack[1][0]) and (stack[0][0] == stack[1][1])
        
        