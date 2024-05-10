class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # iterate from the back
        # pop from stack only if next one is bigger
        
        stack = []
        result = [0] * len(heights)
        
        for i in range(len(heights)-1, -1, -1):
            visible = 0
            
            # if stack exist, and curr is greater
                # pop
                # increment counter
            while stack and heights[i] > stack[-1]:
                stack.pop()
                visible +=1
            
            # if exist
                # increment counter
            if stack:
                visible += 1
            
            # add to result
            # add to stack
            stack.append(heights[i])
            result[i] = visible
        return result