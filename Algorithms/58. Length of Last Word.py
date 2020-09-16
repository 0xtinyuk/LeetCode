class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        found = len(s)
        for i in range(len(s)-1,-1,-1):
            if found==len(s):
                if s[i]!=' ':
                    found=i
            elif s[i]==' ':
                return found-i
        if found == len(s):
            return 0
        else:
            return found+1