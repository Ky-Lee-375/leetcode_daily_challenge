class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right-1:
            middle = (left + right) // 2 
            if nums[middle] < target:
                left = middle
            else:
                right = middle
        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1