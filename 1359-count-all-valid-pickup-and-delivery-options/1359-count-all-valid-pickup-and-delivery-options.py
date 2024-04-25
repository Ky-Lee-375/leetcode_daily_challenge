class Solution:
    def countOrders(self, n: int) -> int:
        # total = 2*n
        # choice for each pair: x(x-1)/2
        
        slots = 2*n
        res = 1
        while (slots > 0):
            choice = slots*(slots-1) //2
            res *= choice
            slots -=2
        
        return res % (10**9 +7)
        
     
        