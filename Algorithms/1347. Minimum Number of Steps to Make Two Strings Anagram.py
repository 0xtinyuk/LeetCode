class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c = [0 for i in range(26)]
        for ch in s:
            c[ord(ch)-97]+=1
        for ch in t:
            c[ord(ch)-97]-=1
        ans = 0
        for i in range(26):
            ans += abs(c[i])
        return ans//2