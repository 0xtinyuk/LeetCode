class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        r = [0 for i in range(60)]
        for x in time:
            r[x%60]+=1
        ans = 0
        if r[0]>1:
            ans += r[0]*(r[0]-1)//2
        if r[30]>1:
            ans += r[30]*(r[30]-1)//2
        for i in range(1,30):
            ans += r[i]*r[60-i]
        return ans