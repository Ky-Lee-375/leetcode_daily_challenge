class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # left, right
        res =[]
        left, right = 0, len(products)-1
        
        products.sort()
        # for each char in searchword
        # while
        for i in range(len(searchWord)):
            c = searchWord[i]
            while left <= right and (len(products[left]) <= i or products[left][i] != c):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != c):
                right -= 1
            
            mid_res = []
            num = min(3, right - left + 1)
            for j in range(num):
                mid_res.append(products[left+j])
            
            res.append(mid_res)
        return res
        