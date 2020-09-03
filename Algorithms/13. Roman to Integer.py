class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        ans = 0
        last = 10000
        for i in range(len(s)):
            if dict[s[i]]>last:
                ans-=2*last
            last = dict[s[i]]
            ans +=last
        return ans