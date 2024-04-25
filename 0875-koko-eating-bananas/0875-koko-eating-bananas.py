class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        l, r = 1, max(piles)
        while l < r:
            middle = (l + r) // 2
            
            hour_spent = 0
            for pile in piles:
                hour_spent += math.ceil(pile/middle)
                
            if hour_spent <= h:
                r = middle
            else:
                l = middle +1
        return r
                
                
        