class Solution:    
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            bin_i = str(bin(i))
            # one_count = 0
            # for j in bin_i:
            #     if j == "1":
            #         one_count+=1
            res.append(bin_i.count('1'))
        return res
            
        
        