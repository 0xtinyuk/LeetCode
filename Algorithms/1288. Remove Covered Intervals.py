class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],-x[1]))
        if len(intervals)<=1:
            return intervals
        current=intervals[0]
        ans=1
        j=1
        while(j<len(intervals)):
            if current[0]<=intervals[j][0] and current[1]>=intervals[j][1]:
                j+=1 
            else:
                current=intervals[j]
                ans+=1
                j+=1
        return ans
    