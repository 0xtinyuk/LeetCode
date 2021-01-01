class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        if len(s)==2:
            if s[0]==s[1]:
                return 3
            return 2
        p = [[False for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            p[i][i]=True
        ans = len(s)
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                p[i][i+1]=True
                ans+=1
        for le in range(3,len(s)+1):
            for i in range(len(s)-le+1):
                if s[i]==s[i+le-1] and p[i+1][i+le-2]:
                    p[i][i+le-1]=True
                    ans+=1
        return ans
                
        