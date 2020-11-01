class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        fl = [[0 for i in range(n)] for j in range(m)]
        fr = [[0 for i in range(n)] for j in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                if s[i-1]==t[j-1]:
                    fl[i][j]=fl[i-1][j-1]+1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if s[i+1]==t[j+1]:
                    fr[i][j]=fr[i+1][j+1]+1
        ans = 0
        for i in range(m):
            for j in range(n):
                if s[i]!=t[j]:
                    ans+=(fl[i][j]+1)*(fr[i][j]+1)
        return ans
                    