class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if(x == 0) and (y == 0):
            return 0
        x = abs(x)
        y = abs(y)
        if x > y:
            t = x
            x = y
            y = t
        if (x == 1) and (y == 1):
            return 2
        if (x == 2) and (y == 2):
            return 4
        if (x == 0) and (y == 1):
            return 3
        if (y <= 2*x):
            return (x+y)//3+(x+y) % 3
        else:
            r = (y-2*x) % 4
            return x+(y-r-2*x)//2+r
