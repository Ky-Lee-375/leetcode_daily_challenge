class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        idx_sum = nums[0]
        if idx_sum >= size-1:
            return True
        for i in range(1, len(nums)):
            if i > idx_sum:
                return False
            idx_sum = max(idx_sum, i+nums[i])
            if idx_sum >= size-1:
                return True  
        return False