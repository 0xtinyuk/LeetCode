class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        m=len(grid)
        n=len(grid[0])
        ans = 0
        def bfs(x,y):
            q = [[x,y]]
            grid[x][y] = '-1'
            l=0
            while l<len(q): 
                for i in range(4):
                    nx = q[l][0] + dx[i]
                    ny = q[l][1] + dy[i]
                    if nx<0 or nx>=m or ny<0 or ny>=n:
                        continue
                    if grid[nx][ny]=='1':
                        grid[nx][ny]='-1'
                        q.append([nx,ny])
                l+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    ans += 1
                    bfs(i,j)
        return ans