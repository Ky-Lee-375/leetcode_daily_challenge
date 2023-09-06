class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        cache = {}
        output = []
        
        for i in range(size):
            if nums[i] in cache:
                output.append(cache[nums[i]])
                continue
                
            pro = 1
            for j in range(size):
                if i != j:
                    pro = pro * nums[j]
            cache[nums[i]] = pro
            output.append(pro)
        return output
