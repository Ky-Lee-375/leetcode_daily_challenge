class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low = 0
        high = len(nums) -1
        while nums[low] > nums[high]:
            mid = (low+high) //2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid +1
        return nums[low]
                
        