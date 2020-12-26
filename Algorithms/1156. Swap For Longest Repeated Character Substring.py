class Solution:
    def maxRepOpt1(self, text: str) -> int:
        ans = 0
        t = [0 for i in range(26)]
        for c in text:
            t[ord(c)-ord('a')]+=1
        f = [[1,1] for i in range(len(text))]
        for i in range(1,len(text)):
            if text[i]==text[i-1]:
                f[i][0]=f[i-1][0]+1
                f[i][1]=min(f[i-1][1]+1,t[ord(text[i])-ord('a')])
            else:
                if i-2>=0 and text[i-2]==text[i]:
                    if f[i-2][0]+2>f[i][1] and f[i-2][0]+2<=t[ord(text[i])-ord('a')]:
                        f[i][1]=f[i-2][0]+2
            if f[i][0]<t[ord(text[i])-ord('a')]:
                if i>=f[i][0] or i<len(text)-1:
                    ans=max(ans,f[i][0]+1)
            ans = max(ans,max(f[i][0],f[i][1]))
        return ans
                        