class Solution:
    def countOrders(self, n: int) -> int:
        # 2n slots per each order: pickup and dropoff
        
        slots = 2*n
        # n *(n-1) /2 -> valid combination
        output = 1
        while slots > 0:
            valid = slots * (slots-1) // 2
            output *= valid
            slots -= 2
        
        return output % (10**9+7)
        
        
     
        