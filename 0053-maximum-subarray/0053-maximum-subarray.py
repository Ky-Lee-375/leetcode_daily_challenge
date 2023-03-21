class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currSum = -math.inf, 0
        for i in range(len(nums)):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
            currSum = max(currSum, 0)
        return maxSum
        
        