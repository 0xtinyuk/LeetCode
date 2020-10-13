class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2)>len(word1):
            word1, word2 = word2, word1
        m=len(word1)
        n=len(word2)
        f=[[0 for j in range(n+1)] for i in range(m+1)]
        longest = 0
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    f[i][j]=max(i,j)
                else:
                    candidate = 1+ min(f[i-1][j-1],min(f[i-1][j],f[i][j-1]))
                    if (word1[i-1]==word2[j-1]):
                        f[i][j]=min(f[i-1][j-1],candidate)
                    else:
                        f[i][j]=candidate
        return f[m][n]