class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        f = [[-1 for i in range(n)] for j in range(n)]
        def dp(i,j):
            if i==j:
                return 1
            if i>j:
                return 0
            if f[i][j] == -1:
                ans = dp(i+1,j) + 1
                if i+1<=j:
                    if arr[i]==arr[i+1]:
                        ans = min(ans,dp(i+2,j)+1)
                for k in range(i+2,j+1):
                    if arr[i]==arr[k]:
                        ans = min(ans,dp(i+1,k-1)+dp(k+1,j))
                f[i][j]=ans
            return f[i][j]
        return dp(0,n-1)