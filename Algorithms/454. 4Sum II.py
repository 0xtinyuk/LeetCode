class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        d = {}
        for x in D:
            for y in C:
                t=x+y
                if t in d:
                    d[t]+=1
                else:
                    d[t]=1
        ans = 0
        for x in A:
            for y in B:
                t = x+y
                if (-t) in d:
                    ans+=d[-t]
        return ans