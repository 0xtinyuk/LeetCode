class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        # end=False
        for i in intervals:
            # if end:
            #     ans.append(i)
            #     continue
            if i[1]<newInterval[0]:
                ans.append(i)
            elif i[0]>newInterval[1]:
                ans.append(newInterval)
                # ans.append(i)
                # end=True
                newInterval=i
            elif i[1]>=newInterval[0] or i[0]<=newInterval[1]:
                newInterval[0]=min(i[0],newInterval[0])
                newInterval[1]=max(i[1],newInterval[1])
        # if not end:
        #     ans.append(newInterval)
        ans.append(newInterval)
        return ans
            
          