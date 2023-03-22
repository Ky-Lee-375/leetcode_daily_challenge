class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_size = len(nums)
        if num_size < 3:
            return []
        nums.sort()
        result = []
        
        for i in range(num_size-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            curr = i
            left = i+1
            right = num_size -1
            
            while (left < right):
                total = nums[curr] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[curr], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left +=1
        return result
            
        
        