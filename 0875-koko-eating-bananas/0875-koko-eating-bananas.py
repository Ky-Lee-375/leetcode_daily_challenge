class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left =1
        right = max(piles)
        # binary search
        while left < right:
            mid = (left+right) // 2
            hours = 0
            for banana in piles:
                hours += math.ceil(banana / mid)
            
            # get the max from the pile
            # start w the middle val
            if hours <= h:
                right = mid
            else:
                left = mid +1
        return right