class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # sort products -> lexicographical
        products.sort()
        
        # use two pointers l and r
        l, r = 0, len(products) -1
        
        # final list
        res = []
        # move l and r as it doesnt match w prefix
        for i in range(len(searchWord)):
            c = searchWord[i]
            # while for moving l
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            # while for moving r
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1
            res.append([])
        # if it does match, add to the final list
            # add first three, if less, add all
            remain = r -l +1
            j = min(remain, 3)
            for k in range(j):
                res[-1].append(products[l+k])
        # return a list of lists
        return res