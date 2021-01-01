class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        f = [0 for i in range(300)]
        if k==0:
            return 0
        l=0
        r=0
        f[ord(s[0])]+=1
        distinct = 1
        ans = 1
        while r<len(s):
            if l>r or distinct<=k:
                r+=1
                if r>=len(s):
                    break
                f[ord(s[r])]+=1
                if f[ord(s[r])]==1:
                    distinct+=1
                if distinct<=k and (r-l+1)>ans:
                    ans = r-l+1
            else:
                f[ord(s[l])]-=1
                if f[ord(s[l])]==0:
                    distinct-=1
                l+=1
        return ans