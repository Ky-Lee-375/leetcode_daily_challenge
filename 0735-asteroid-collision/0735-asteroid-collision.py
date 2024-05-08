class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack
        # neg: left, pos: right
        stack = []
        
        for a in asteroids:
            # while stack exist
            # current is neg and last of stack is postive
            # collision happen
            while stack and a <0 and stack[-1] > 0:
                diff = a + (stack[-1])
                # if sum is neg: keep neg
                if diff < 0:
                    stack.pop()
                # if sum is pos: keep pos
                elif diff > 0:
                    a = 0
                # is sum is 0: pop both
                else:
                    a = 0
                    stack.pop()
            if a != 0:
                stack.append(a)
        return stack
            