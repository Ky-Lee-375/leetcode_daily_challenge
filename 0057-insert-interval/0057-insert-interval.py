class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: 
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort()
        
        result=[]
        result.append(intervals[0])
        
        for i in intervals[1:]:
            if i[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1],i[1])
            else:
                result.append(i)               
        return result
        