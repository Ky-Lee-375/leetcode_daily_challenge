class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) //2
            
            hour_spent = 0
            for p in piles:
                hour_spent += math.ceil(p/mid)
            
            if hour_spent <= h:
                right = mid
            else:
                left = mid +1
        return right
        