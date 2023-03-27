class Solution:
    def rob(self, nums: List[int]) -> int:        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        sumlist = [0] * (len(nums))
        sumlist[0] = nums[0]
        sumlist[1] = max(nums[0], nums[1])
        
        for i in range(2,len(nums)):
            sumlist[i] += max(sumlist[i-1], sumlist[i-2]+nums[i])
        return sumlist[-1]