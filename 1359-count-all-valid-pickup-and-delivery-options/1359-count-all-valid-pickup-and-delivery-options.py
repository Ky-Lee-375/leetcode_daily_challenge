class Solution:
    def countOrders(self, n: int) -> int:
        # 2n slots: pickup and dropoff
        # x*(x-1)/2 -> valid choices
        
        slots = 2*n
        output = 1
        while slots > 0:
            valid = slots*(slots-1)//2
            output *= valid
            slots -= 2
        return output % (10**9 +7)
        