class Solution:
    def isNumber(self, s: str) -> bool:
        e=False
        dot=False
        int_num=False
        sign=False
        i=0
        n=len(s)
        while i<n and s[i]==' ':
            i+=1
        while i<n and s[n-1]==' ':
            n-=1
        while i<n:
            c=s[i]
            if c=='-' or c=='+':
                if sign:
                    return False
                sign=True
            elif c=='.':
                if dot:
                    return False
                dot=True
                sign=True
            elif c=='e':
                if e or (not int_num):
                    return False
                e=True
                sign=False
                dot=True
                int_num=False
            elif c>='0' and c<='9':
                int_num=True
                sign=True
            else:
                return False
            i+=1
        if not int_num:
            return False
        return True