class Solution:
    def gcd(self, a: int, b: int) -> int:
        if (b == 0):
            return a
        return self.gcd(b, a % b)

    def lcm(self, a: int, b: int) -> int:
        return a*b//self.gcd(a, b)

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l = 1
        r = 2000000000
        while(l < r):
            mid = (l+r)//2
            s = (mid//a)+(mid//b)+(mid//c)\
                - (mid//self.lcm(a, b))-(mid//self.lcm(b, c))-(mid//self.lcm(a, c))\
                + (mid//self.lcm(a, self.lcm(b, c)))
            if (s < n):
                l = mid+1
            else:
                r = mid
        return l
