class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        deck = {}
        for i in range(len(nums)):
            if nums[i] in deck:
                return deck[nums[i]], i
            else:
                leftover = target - nums[i]
                deck[leftover] = i
        return -1,-1