class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal and (len(set(s)) < len(s)):
                return True
        stack = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                stack.append((s[i], goal[i]))

        return len(stack) ==2 and (stack[0][0] == stack[1][1]) and (stack[0][1] == stack[1][0])
            
        