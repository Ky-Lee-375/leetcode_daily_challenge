class Solution:
    def climbStairs(self, n: int) -> int:
        # if (n <= 2):
        #     return n
        fibo = {}
        
        fibo[1] = 1
        fibo[2] = 2
        
        for i in range(3,n+1):
            fibo[i] = fibo[i-1] + fibo[i-2]
            
        return fibo[n]
            
    
    
        