class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # monotonic stack
        stack = []
        res = [0] * len(heights)
        
        # loop backward
        for i in range(len(heights)-1, -1, -1):
            visible = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                visible += 1
            
            if stack:
                visible += 1
            
            res[i] = visible
            stack.append(heights[i])
                
        return res
        