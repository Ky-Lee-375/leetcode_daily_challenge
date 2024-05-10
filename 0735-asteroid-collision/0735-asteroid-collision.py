class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack
        stack = []
    
        # if neg after pos -> find diff
        # if neg -> neg win
        # if pos -> pos win
        # if 0 -> pop both
        
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = stack[-1] + a
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a =0
                else:
                    a = 0
                    stack.pop()
            if a != 0:
                stack.append(a)
        return stack