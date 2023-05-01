class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        
        total = sum(nums)
        if total % 2 != 0: 
            return False
        target = total//2
        s = {target}
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            else:
                to_add = set()
                for ele in s:
                    if ele >= nums[i]:
                        to_add.add(ele-nums[i])
                s = s.union(to_add)
        
        return False