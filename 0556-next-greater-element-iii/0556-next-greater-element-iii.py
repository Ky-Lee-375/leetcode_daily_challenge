class Solution:
    def nextGreaterElement(self, n: int) -> int:
        size = len(str(n))
        idx = size -2
        n_arr = [c for c in str(n)]
        
        if size == 1:
            return -1
        
        while idx >= 0 and n_arr[idx] >= n_arr[idx+1]:
            idx -= 1
        
        if idx < 0:
            return -1
        
        j = size -1
        while n_arr[idx] >= n_arr[j]:
            j -=1
        n_arr[idx], n_arr[j] = n_arr[j], n_arr[idx]
        n_arr[idx+1:] = reversed(n_arr[idx+1:])
        
        res = ''.join(n_arr)
        return int(res) if int(res) < 2**31 else -1
        
        # start from the back
        # find the first decreasing point
        # swap with next greates
        # sort the rest
        