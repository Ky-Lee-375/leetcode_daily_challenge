"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # from schedule
        # merge the intervals
        intervals = []
        for employee in schedule:
            for time in employee:
                start_ = time.start
                end_ = time.end
                intervals.append([start_, end_])
        # sort the interval in increasing order
        intervals.sort(key = lambda x:x[0])
        
        # if start of next is smaller than end of first
        # we can merge
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            prev = merged[-1]
            curr = intervals[i]
            
            if curr[0] <= prev[1]:
                # merge
                merged[-1] = [prev[0], max(prev[1], curr[1])]
            else:
                merged.append(curr)
        
        # go through the merged list and append the gap
        free = []
        for i in range(len(merged)-1):
            free.append(Interval(merged[i][1], merged[i+1][0]))
        return free
            