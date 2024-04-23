class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        s_list = [c for c in s]
        l = len(s)
        
        if l == 1:
            return -1
        idx = l-2
        while idx >= 0 and s_list[idx] >= s_list[idx+1]:
            idx -= 1
            
        if idx < 0:
            return -1
        
        j = l-1
        while s_list[j] <= s_list[idx]:
            j -= 1
        
        s_list[idx], s_list[j] = s_list[j], s_list[idx]
        s_list[idx+1:] = reversed(s_list[idx+1:])
        
        # *** .join is required to convert back to string ***
        ans = ''.join(s_list)
        return int(ans) if int(ans) < 2**31 else -1
        