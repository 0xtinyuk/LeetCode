class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board)==0:
            return False
        self.word = word
        self.board = board
        self.n=len(board)
        self.m=len(board[0])
        self.mark=[[False for j in range(self.m)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j]==word[0] and self.search(i,j,0):
                    return True
        return False
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    def search(self,x:int,y:int,k:int):
        if k>=len(self.word)-1:
            return True
        self.mark[x][y]=True
        for i in range(4):
            nx=self.dx[i]+x
            ny=self.dy[i]+y
            if nx<0 or nx>=self.n or ny<0 or ny>=self.m:
                continue
            if (self.mark[nx][ny])or(self.board[nx][ny]!=self.word[k+1]):
                continue
            if self.search(nx,ny,k+1):
                return True
        self.mark[x][y]=False
        return False
        