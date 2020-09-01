class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        ans = s[0]
        for i in range(len(s)):
            half_length = 1
            while(i-half_length>=0 and i+half_length<len(s)):
                l=i-half_length
                r=i+half_length
                if s[l]!=s[r]:
                    break
                temp = s[l:r+1]
                if len(temp)>len(ans):
                    ans=temp
                half_length+=1
            if (i+1<len(s)) and s[i]==s[i+1]:
                half_length = 0
                while(i-half_length>=0 and i+half_length+1<len(s)):
                    l=i-half_length
                    r=i+1+half_length
                    if s[l]!=s[r]:
                        break
                    temp = s[l:r+1]
                    if len(temp)>len(ans):
                        ans=temp
                    half_length+=1
        return ans