class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dic = {}
        for c in coins:
            dic[c] = 1
        for v in range(1,amount+1):
            for s in coins:
                diff = v - s
                if v - s in dic:
                    if v not in dic:
                        dic[v] = dic[v-s] +1
                    else:
                        dic[v] = min(dic[v],dic[v-s]+1)
        if amount not in dic:
            return -1
        else:
            return dic[amount]
        
        