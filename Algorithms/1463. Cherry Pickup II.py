class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        d1=[-1,-1,-1,0,0,0,1,1,1]
        d2=[-1,0,1,-1,0,1,-1,0,1]
        f=[[-1 for i in range(n)] for j in range(n)]
        f[0][n-1]=grid[0][0]+grid[0][n-1]
        for i in range(1,m):
            temp = [[-1 for i in range(n)] for j in range(n)]
            for j in range(n):
                for k in range(n):
                    if f[j][k]!=-1:
                        for direction in range(9):
                            nj=j+d1[direction]
                            nk=k+d2[direction]
                            if nj>=0 and nj<n and nk>=0 and nk<n:
                                if nj==nk:
                                    temp[nj][nk]=max(temp[nj][nk],f[j][k]+grid[i][nj])
                                else:
                                    temp[nj][nk]=max(temp[nj][nk],f[j][k]+grid[i][nj]+grid[i][nk])
            f = temp
        ans = 0
        for j in range(n):
            for k in range(n):
                if f[j][k]>ans:
                    ans = f[j][k]
        return ans