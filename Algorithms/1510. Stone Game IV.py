class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        f = [False,True]
        for i in range(2,n+1):
            j=1
            f.append(False)
            while i-j*j>=0:
                if not f[i-j*j]:
                    f[i]=True
                    break
                j+=1
        return f[n]
