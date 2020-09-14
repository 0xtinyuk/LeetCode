class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mark=[[False for i in range(9)] for j in range(9)]
        for i in range(9):
            row=[False for i in range(9)]
            col=[False for i in range(9)]
            for j in range(9):
                if board[i][j]!=".":
                    num = int(board[i][j])-1
                    if row[num]:
                        return False
                    row[num]=True
                    k=(i//3)*3+(j//3)
                    if mark[k][num]:
                        return False
                    mark[k][num]=True
                if board[j][i]!=".":
                    num = int(board[j][i])-1
                    if col[num]:
                        return False
                    col[num]=True  
        return True