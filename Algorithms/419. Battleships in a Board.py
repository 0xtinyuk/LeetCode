class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X':
                    if j-1>=0 and board[i][j-1]=='X':
                        continue
                    if i-1>=0 and board[i-1][j]=='X':
                        continue
                    ans +=1
        return ans