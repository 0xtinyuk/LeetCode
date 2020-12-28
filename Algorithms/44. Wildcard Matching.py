class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for i in range(0,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='*':
                    dp[i][j] = dp[i][j] or ((i>0) and dp[i-1][j]) or dp[i][j-1] or ((i>0) and dp[i-1][j-1])
                if i>0:
                    if s[i-1]==p[j-1] or p[j-1]=='?':
                        dp[i][j] = dp[i][j] or dp[i-1][j-1]
        return dp[len(s)][len(p)]