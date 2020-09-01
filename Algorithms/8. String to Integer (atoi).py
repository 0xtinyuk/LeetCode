class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        i = 0
        positive = True
        while i<len(str):
            ch = str[i]
            if ch ==' ':
                i +=1
                continue
            if (ch=='+' or ch=='-'):
                i+=1
                if ch=='-':
                    positive=False
                break
            if (ch>='0' and ch<='9'):
                break
            return 0
        counter = 0
        ans = 0
        while (i<len(str)):
            ch = str[i]
            if (ch>='0' and ch<='9'):
                ans = ans*10+ord(ch)-48
                if ans>0:
                    counter +=1
                if counter >10:
                    break
                i+=1
            else:
                break
        if not positive:
            ans=-ans
        if ans>((1<<31)-1):
            ans = (1<<31) -1
        if ans<(-(1<<31)):
            ans = - (1<<31)
        return ans
        
        
            