class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points,key=lambda x:x[1])
        if len(points)<=0:
            return 0
        ans=1
        last = points[0][1]
        for i in range(1,len(points)):
            if points[i][0]<=last:
                continue
            ans+=1
            last = points[i][1]
        return ans