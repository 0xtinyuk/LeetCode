class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        m=len(board)
        n = len(board[0])
        mark = [[False for j in range(n)] for i in range(m)]
        def dfs(x,y,word):
            if len(word)==0:
                return True
            mark[x][y]=True
            ne = word[1:]
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or nx>=m or ny<0 or ny>=n:
                    continue
                if (not mark[nx][ny]) and (board[nx][ny]==word[0]):
                    if dfs(nx,ny,ne):
                        mark[x][y]=False
                        return True
            mark[x][y]=False
            return False
        ans = set()
        for i in range(m):
            for j in range(n):
                for w in words:
                    if not (w in ans):
                        if w[0]==board[i][j] and dfs(i,j,w[1:]):
                            ans.add(w)
        return list(ans)