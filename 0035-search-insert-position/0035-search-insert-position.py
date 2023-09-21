class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        elif target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else: 
            left = 0
            right = len(nums)-1

            while left != right -1:
                mid = (left+right) // 2
                if target > nums[mid]:
                    left = mid 
                elif target < nums[mid]:
                    right = mid
                else:
                    return mid
            return right
        