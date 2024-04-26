class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # edge case:
        if len(arr) == k:
            return arr
        
        # binary search
        # find the index of the closest occurrence
        idx = bisect.bisect_left(arr, x)
        # *** left could be -1
        left, right = idx -1, idx
        
        # two pointers: left and right
        # while right - left - 1 < k
        # if |left-x| < |right-x|
            # increment right
        while right - left -1 < k:
            if left == -1:
                right += 1
                continue
            if right == len(arr) or (left >=0 and abs(arr[left]-x) <= abs(arr[right]-x)):
                left -=1
            else:
                right += 1
            
        # slice from left to right
        # return that array
        return arr[left+1:right]