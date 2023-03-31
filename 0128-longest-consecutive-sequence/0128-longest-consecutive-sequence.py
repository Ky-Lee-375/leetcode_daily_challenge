class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        total = 0
        
        for elem in nums:
            if (elem-1) not in nums:
                length = 1
                while (elem+1) in nums:
                    length += 1
                    elem += 1
                total = max(length, total) 
        return total