class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend ==0 :
            return 0
        (r,ans) = self.find(abs(dividend),abs(divisor),1)
        if(r>=abs(divisor)):
            ans+=1
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            ans=-ans
        if ans>((1<<31)-1) or ans<(-(1<<31)):
            return (1<<31)-1
        return ans

    def find(self,dividend:int,divisor:int,temp:int)->(int,int):
        if divisor>dividend:
            return (dividend,0)
        if dividend-divisor<divisor:
            return (dividend-divisor,temp)
        (d,ans) = self.find(dividend,divisor+divisor,temp+temp)
        if d>divisor:
            d-=divisor
            ans+=temp
        return (d,ans)