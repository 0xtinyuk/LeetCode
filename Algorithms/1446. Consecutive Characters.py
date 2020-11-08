class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        t=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                t+=1
            else:
                if t>ans:
                    ans=t
                t=1
        if t>ans:
            ans = t
        return ans