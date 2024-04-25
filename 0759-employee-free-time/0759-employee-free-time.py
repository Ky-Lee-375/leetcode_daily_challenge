"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        # put data in a list form -> easy to handle and modify
        for employee in schedule:
            for worktime in employee:
                start_ = worktime.start
                end_ = worktime.end
                intervals.append([start_, end_])
        # sort the interval array
        intervals.sort(key = lambda x:x[0])
        
        merged = [intervals[0]]
        # go through it and see if we can merge
        # merged list
        for i in range(1, len(intervals)):
            prev = merged[-1]
            curr = intervals[i]
            
            if curr[0] <= prev[1]:
                # we merge it
                merged[-1] = [prev[0], max(prev[1], curr[1])]
            else:
                merged.append(curr)
        # go through merged list
        # append the gap bwt every interval
        if len(merged) <= 1:
            return []
        res = []
        for i in range(len(merged)-1):
            res.append(Interval(merged[i][1], merged[i+1][0]))
        return res
        
    
    
    

# O(n log N)
    