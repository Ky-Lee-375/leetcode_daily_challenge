class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        lst = []
        
        def backtrack(cur):
            if len(cur) == len(nums):
                lst.append(cur[:])
                return
            
            for n in nums:
                if n not in cur:
                    cur.append(n)
                    backtrack(cur)
                    cur.pop()
        
        backtrack([])
        return lst