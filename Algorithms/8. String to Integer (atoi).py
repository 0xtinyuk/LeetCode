class Solution:
    def myAtoi(self, s: str) -> int:
        positive = True
        i = 0
        while i<len(s) and s[i]==' ':
            i+=1
        if i==len(s):
            return 0
        if s[i]=='+' or s[i]=='-':
            if s[i]=='-':
                positive = False
            i+=1
        ans = 0
        while i<len(s):
            if s[i]>='0' and s[i]<='9':
                ans = ans*10+ord(s[i])-ord('0')
                if ans>((1<<31)-1) and positive:
                    return (1<<31)-1
                if ans>((1<<31)) and (not positive):
                    return -(1<<31)
            else:
                break
            i+=1
        if not positive:
            ans = -ans
        return ans