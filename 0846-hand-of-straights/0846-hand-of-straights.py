class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
            if len(hand) == 0:
                return False
            
            handDict = defaultdict(int)
            for x in hand:
                handDict[x] += 1
    
            while handDict:
                start = min(handDict.keys())
                handDict[start] -= 1
                if handDict[start] == 0:
                    handDict.pop(start)

                for i in range(start+1, start+groupSize):
                    if i not in handDict:
                        return False
                    handDict[i] -= 1
                    if handDict[i] == 0:
                        handDict.pop(i)
            return True
