class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # f = [[False for y in range(len(s)+1)] for x in range(len(p)+1)]
        # f[0][0]=True
        f=[False for y in range(len(s)+1)]
        f[0]=True
        i=0
        while i<len(p):
            n=[False for y in range(len(s)+1)]
            if i+1<len(p) and p[i+1]=='*':
                for j in range(len(s)):
                    if (f[j] or n[j]):
                        n[j]=True 
                        if p[i]=='.' or s[j]==p[i]:
                            n[j+1]=True
                if f[len(s)]:
                    n[len(s)]=True
                i+=2
            else:
                updated = False
                for j in range(len(s)):
                    if (f[j])and(p[i]=='.' or s[j]==p[i]):
                        n[j+1]=True
                        updated=True
                if not updated:
                    return False
                i+=1
            f=n
        return f[len(s)]