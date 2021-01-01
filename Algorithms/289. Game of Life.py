class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                t = 0
                for di in range(-1,2):
                    for dj in range(-1,2):
                        nx = i+di
                        ny = j+dj
                        if nx<0 or nx>=m or ny<0 or ny>=n:
                            continue
                        if nx==i and ny==j:
                            continue
                        if board[nx][ny]==1 or board[nx][ny]==-1:
                            t+=1
                if t<2 or t>3:
                    if board[i][j]==1:
                        board[i][j]=-1
                if t==3:
                    if board[i][j]==0:
                        board[i][j]=2
        for i in range(m):
            for j in range(n):
                if board[i][j]==2:
                    board[i][j]=1
                if board[i][j]==-1:
                    board[i][j]=0
        return