class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0, len(arr) - k
        while low < high:
            mid = (low + high) // 2
            # Shift the window to right if the element at mid+k is closer or the same distance but higher than arr[mid]
            if x - arr[mid] > arr[mid + k] - x:
                low = mid + 1
            else:
                high = mid
        # can manually build it as well: O(log (n-k))
        return arr[low:low + k]