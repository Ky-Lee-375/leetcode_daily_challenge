class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # declare res array
        res = []
        
        # maintain two pointers
        # left, right
        left, right = 0, len(products)-1
        
        # sort the array
        products = sorted(products)
        
        # go through letter in searchWord
        # if it matches
        # add first three or min (right - left +1)
        # apped to the res
        for i in range(len(searchWord)):
            c = searchWord[i]
            while left <= right and (len(products[left]) <= i or c != products[left][i]):
                left += 1
            while left <= right and (len(products[right]) <= i or c != products[right][i]):
                right -= 1
            
            res.append([])
            remain = min(3, right-left+1)
            for j in range(remain):
                res[-1].append(products[left+j])
            
        return res
        # return res
        