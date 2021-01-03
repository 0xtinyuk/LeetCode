class Solution:
    def smallestSubsequence(self, s: str) -> str:
        if len(s)==0:
            return ""
        c = [0 for i in range(26)]
        t = 0
        for ch in s:
            c[ord(ch)-97]+=1
            if c[ord(ch)-97]==1:
                t+=1
        pos = len(s)
        c = [0 for i in range(26)]
        for i in range(len(s)-1,-1,-1):
            c[ord(s[i])-97]+=1
            if c[ord(s[i])-97]==1:
                t-=1
                if t==0:
                    pos = i
                    break
        for i in range(pos-1,-1,-1):
            if s[i]<=s[pos]:
                pos = i
        temp = s[pos+1:].replace(s[pos],"")
        return s[pos]+self.smallestSubsequence(temp)