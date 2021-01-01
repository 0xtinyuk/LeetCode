class Solution:
    def reverseWords(self, s: str) -> str:
        curStart = 0
        s = list(s)
        for i in range(len(s)):
            if s[i]==" ":
                j=curStart
                k=i-1
                while j<k:
                    temp = s[j]
                    s[j]=s[k]
                    s[k]=temp
                    j+=1
                    k-=1
                curStart = i+1
        if curStart<len(s):
            j=curStart
            k=len(s)-1
            while j<k:
                temp = s[j]
                s[j]=s[k]
                s[k]=temp
                j+=1
                k-=1
        return "".join(s)