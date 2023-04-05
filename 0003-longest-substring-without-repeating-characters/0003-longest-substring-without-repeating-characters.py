class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        queue = deque()
        items = {}
        longest = 0
        
        for c in s:
            if c in items:
                popped = None
                while popped != c:
                    popped = queue.popleft()
                    if popped in items:
                        items.pop(popped)
            queue.append(c)
            items[c] = c
                
            longest = max(longest, len(queue))
        
        return longest
        