class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        s = 0
        n = 0
        while s<target:
            n+=1
            s+=n
        if ((n+1)//2)%2==target%2:
            return n
        if ((n+2)//2)%2==target%2:
            return n+1
        if ((n+3)//2)%2==target%2:
            return n+2
        return 0