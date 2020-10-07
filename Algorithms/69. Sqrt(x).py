class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l=2
        r=x//2
        while(l<r):
            mid=(l+r)//2
            if mid*mid>x:
                r=mid-1
            elif mid*mid==x:
                return mid
            else:
                if (mid+1)*(mid+1)>x:
                    return mid
                l=mid+1
        return r      