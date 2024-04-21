"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervalsArray = []
        for employee in schedule:
            for workTime in employee:
                start = workTime.start
                end = workTime.end
                intervalsArray.append([start,end])
        intervalsArray.sort(key = lambda x :x[0])
        
        mergedArray = [intervalsArray[0]]
        for idx in range(1, len(intervalsArray)):
            prevWork = mergedArray[-1]
            currWork = intervalsArray[idx]
            
            if currWork[0] <= prevWork[1]:
                start = prevWork[0]
                end = max(prevWork[1], currWork[1])
                mergedArray[-1] = [start,end]
            else:
                mergedArray.append(currWork)
        
        result = []
        if len(mergedArray) <=1:
            return result
        
        for i in range(len(mergedArray) -1):
            start = mergedArray[i][1]
            end = mergedArray[i+1][0]
            result.append(Interval(start,end))
        
        return result
        