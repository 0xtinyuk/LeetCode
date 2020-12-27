class Solution:
    def knightDialer(self, n: int) -> int:
        d = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]
        f = [[1,1,1,1,1,1,1,1,1,1]] + [[0,0,0,0,0,0,0,0,0,0] for i in range(n-1)]
        ans = 0
        def search(cur:int,n:int) -> int:
            if f[n][cur]==0:
                ans = 0
                for i in d[cur]:
                    ans = (ans + search(i,n-1)) % 1000000007
                f[n][cur] = ans
            return f[n][cur]
        for i in range(10):
            ans = (ans + search(i,n-1)) % 1000000007
        return ans