class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            cur = ord(s[i])-ord('A')+1
            ans += cur * int(pow(26,len(s)-i-1))
        return ans