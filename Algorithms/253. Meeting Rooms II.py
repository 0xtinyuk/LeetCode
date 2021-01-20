class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        s = [intervals[i][0] for i in range(len(intervals))]
        e = [intervals[i][1] for i in range(len(intervals))]
        s = sorted(s)
        e = sorted(e)
        ans = 0
        i = 0
        j = 0
        while i<len(intervals):
            if s[i]<e[j]:
                ans+=1
            else:
                j+=1
            i+=1
        return ans
        