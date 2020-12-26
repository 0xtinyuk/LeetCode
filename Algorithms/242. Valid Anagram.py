class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a = [0 for i in range(26)]
        for c in s:
            a[ord(c)-ord('a')]+=1
        for c in t:
            a[ord(c)-ord('a')]-=1
            if a[ord(c)-ord('a')]<0:
                return False
        return True
        