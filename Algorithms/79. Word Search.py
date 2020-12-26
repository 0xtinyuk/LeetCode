class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        m=len(board)
        n=len(board[0])
        mark = [[False for j in range(len(board[0]))]for i in range(len(board))]
        def dfs(x:int,y:int,word:str)-> bool:
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or nx>=m or ny<0 or ny>=n:
                    continue
                if mark[nx][ny] or (board[nx][ny]!=word[0]):
                    continue
                if len(word)==1:
                    return True
                mark[nx][ny]=True
                if dfs(nx,ny,word[1:]):
                    return True
                mark[nx][ny]=False
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if len(word)==1:
                        return True
                    mark[i][j]=True
                    if dfs(i,j,word[1:]):
                        return True
                    mark[i][j]=False
        return False