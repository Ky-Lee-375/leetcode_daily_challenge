class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup_dict={}

        for i in nums:
            if i in dup_dict:
                dup_dict[i] = dup_dict[i]+1
            else:
                dup_dict[i] = 1
        
        for item in dup_dict:
            if dup_dict[item] >= 2:
                return item
        return -1
