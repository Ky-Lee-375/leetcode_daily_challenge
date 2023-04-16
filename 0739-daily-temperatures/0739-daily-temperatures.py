class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                cur, idx = stack.pop()
                temperatures[idx] = i - idx
            stack.append((temperatures[i], i))
        
        while stack:
            cur, idx = stack.pop()
            temperatures[idx] = 0
        
        return temperatures
        