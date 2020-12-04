class Solution:
    def calculate(self, s: str) -> int:
        cur = 0
        ans = 0
        last = 0
        sign = '+'
        for x in s:
            if x==' ':
                continue
            if x>='0' and x<='9':
                cur=cur*10+ord(x)-ord('0')
                continue
            if sign=='+' or sign=='-':
                ans = ans + last
                if sign=='+':
                    last = cur
                else:
                    last = -cur     
            elif sign=='*':
                last = last * cur
            else:
                last = int(last/cur)
            cur = 0
            sign = x
        if sign=='+' or sign=='-':
            ans = ans + last
            if sign=='+':
                last = cur
            else:
                last = -cur
        elif sign=='*':
            last = last * cur
        else:
            last = int(last/cur)
        ans = ans + last
        return ans
        

