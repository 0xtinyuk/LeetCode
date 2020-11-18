class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if (p/q)==(p//q):
            if (p//q)%2==0:
                return 2
            else:
                return 1
        h = p
        v = q
        while v%p!=0:
            v+=q
            h=p-h
            if v>2*p:
                v-=2*p
        if v==p:
            if h==0:
                return 2
            else:
                return 1
        else:
            return 0