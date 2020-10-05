class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)<len(b):
            a,b=b,a
        plus=0
        j=len(b)-1
        ans = ""
        for i in range(len(a)-1,-1,-1):
            x=int(a[i])
            if j>=0:
                y=int(b[j])
                j-=1
            else:
                y=0
            temp=x+y+plus
            if temp>=2:
                plus=1
                temp-=2
            else:
                plus=0
            ans=str(temp)+ans
        if plus==1:
            ans = "1"+ans
        return ans
            
