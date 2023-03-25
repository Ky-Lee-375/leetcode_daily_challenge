class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp_arr = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp_arr[i] < dp_arr[j] + 1:
                    dp_arr[i] = dp_arr[j] +1
        return max(dp_arr)