class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search
        # find the target number
        if len(arr) == k:
            return arr
        n = len(arr)
        idx = bisect.bisect_left(arr, x)
        left, right = idx -1, idx
        
        while right - left -1 < k:
            if left == -1:
                right += 1
                continue
            if right == n or (left>=0 and abs(arr[left] - x) <= abs(arr[right]-x)):
                # left is closer to x than right
                left -= 1
            else:
                right += 1
        print(left, right)
        return arr[left+1:right]