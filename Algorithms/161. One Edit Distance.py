class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s)<len(t):
            s,t = t,s
        if len(s)-len(t)>1:
            return False
        if len(s)==len(t):
            diff = 0
            for i in range(len(s)):
                if s[i]!=t[i]:
                    diff+=1
            if diff!=1:
                return False
            return True
        if len(t)==0:
            return True
        lf = [False for i in range(len(s))]
        rf = [False for i in range(len(s))]
        for i in range(len(s)-1):
            if s[i]==t[i]:
                lf[i]=True
            else:
                break
        for i in range(len(s)-1,0,-1):
            if s[i]==t[i-1]:
                rf[i]=True
            else:
                break
        print(lf)
        print(rf)
        if lf[len(s)-2]:
            return True
        if rf[1]:
            return True
        for i in range(1,len(s)-1):
            if lf[i-1] and rf[i+1]:
                return True
        return False
            