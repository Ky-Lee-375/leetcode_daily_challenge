class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # convert to string
        s = str(n)
        # convert to list
        s_list = [c for c in s]
        size = len(s_list)
        
        # no next greater
        if size == 1:
            return -1
        
        # find the first non increasing point
        idx = size -2
        while idx >= 0 and s_list[idx] >= s_list[idx+1]:
            idx -= 1
        if idx == -1:
            return -1
                
        # find the next largest
        j = size -1
        while s_list[j] <= s_list[idx]:
            j -= 1

        # swap
        s_list[idx], s_list[j] = s_list[j], s_list[idx]
        # reverse the rest increasing order
        s_list[idx+1:] = reversed(s_list[idx+1:])
        
        ans = ''.join(s_list)
        # return int
        # chck if it's 32 bit int
        return int(ans) if int(ans) < 2**31 else -1