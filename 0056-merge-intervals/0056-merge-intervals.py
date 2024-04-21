class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals
        intervals.sort(key = lambda x:x[0])
        # iterate through array
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        
        return merged
        