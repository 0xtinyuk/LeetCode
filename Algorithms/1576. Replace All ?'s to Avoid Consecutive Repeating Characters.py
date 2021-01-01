class Solution:
    def modifyString(self, s: str) -> str:
        s=list(s)
        for i in range(len(s)):
            if s[i]=="?":
                t = 97
                if i>0 and ord(s[i-1])==t:
                    t+=1
                if i+1<len(s) and ord(s[i+1])==t:
                    t+=1
                if i>0 and ord(s[i-1])==t:
                    t+=1
                s[i]=chr(t)
        return "".join(s)   