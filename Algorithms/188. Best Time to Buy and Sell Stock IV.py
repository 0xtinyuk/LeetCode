class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        NEG_INF = -(1<<31)
        if len(prices)==0 or k==0:
            return 0
        n = len(prices)
        if 2*k>=n:
            ans = 0
            for i in range(1,n):
                ans +=max(0,prices[i]-prices[i-1])
            return ans
        f = [[[NEG_INF,NEG_INF] for j in range(k+1)] for i in range(n)]
        f[0][0][0]=0
        f[0][1][1]=-prices[0]
        for i in range(1,n):
            for j in range(k+1):
                f[i][j][0] = max(f[i-1][j][1]+prices[i],f[i-1][j][0])
                if j>0:
                    f[i][j][1] = max(f[i-1][j][1],f[i-1][j-1][0]-prices[i])
        ans = 0
        for i in range(k+1):
            ans = max(ans,f[n-1][i][0])
        return ans