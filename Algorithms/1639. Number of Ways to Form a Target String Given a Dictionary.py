class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(words[0])
        m = len(target)
        if n<m:
            return 0
        count = [[0 for i in range(26)] for j in range(n)]
        for i in range(len(words)):
            for j in range(n):
                count[j][ord(words[i][j])-97]+=1
        cur = [0 for i in range(n)]
        for i in range(n):
            cur[i]=count[i][ord(target[0])-97]
        for i in range(1,m):
            last = cur
            cur = [0 for i in range(n)]
            s = last[i-1]
            for j in range(i,n):
                if count[j][ord(target[i])-97]>0:
                    cur[j]=(s*count[j][ord(target[i])-97])%1000000007
                s=(s+last[j])%1000000007
        ans = 0
        for i in range(m-1,n):
            ans = (ans + cur[i])%1000000007
        return ans