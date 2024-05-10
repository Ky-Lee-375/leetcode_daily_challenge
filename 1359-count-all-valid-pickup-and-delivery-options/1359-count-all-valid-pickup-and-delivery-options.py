class Solution:
    def countOrders(self, n: int) -> int:
        # total
        # 2*n
        total = 2*n
        # while n exists
        # for each slot: n (n-1) //2 
        # return modulo
        ans = 1
        while total > 0:
            choices = total * (total-1) //2
            ans *= choices
            total -=2
        return ans % (10**9 + 7)