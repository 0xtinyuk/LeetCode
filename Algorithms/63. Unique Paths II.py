class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        if m<=0:
            return 0
        n=len(obstacleGrid[0])
        if n<=0:
            return 0
        obstacleGrid[0][0]=1-obstacleGrid[0][0]
        for i in range(1,n):
            obstacleGrid[0][i]=min(obstacleGrid[0][i-1],1-obstacleGrid[0][i])
        for i in range(1,m):
            obstacleGrid[i][0]=min(obstacleGrid[i-1][0],1-obstacleGrid[i][0])
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=0
                else:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]       