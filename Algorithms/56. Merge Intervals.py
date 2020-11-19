class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[1], x[0]))
        ans = []
        for i in intervals:
            temp = i
            for j in range(len(ans)-1, -1, -1):
                if ans[j][1] >= temp[0]:
                    temp[1] = max(ans[j][1], temp[1])
                    temp[0] = min(ans[j][0], temp[0])
                    ans.pop(j)
                else:
                    break
            ans.append(temp)
        return ans