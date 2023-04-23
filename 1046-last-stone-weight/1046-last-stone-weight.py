class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_size = len(stones)
        if stone_size == 0:
            return 0
        
        while stone_size != 1:
            tmp_max_1 = max(stones)
            stones.remove(max(stones))
            tmp_max_2 = max(stones)
            stones.remove(max(stones))
            ans = abs(tmp_max_1-tmp_max_2)
            stones.append(ans)
            
            stone_size = len(stones)
        return stones[0]
        