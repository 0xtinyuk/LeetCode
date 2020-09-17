class Solution {
    public void solveSudoku(char[][] board) {
        solve(board);
    }

    private boolean solve(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') continue;
                for (int k = 1; k <= 9; k++) {
                    char ch=(char)(k+48);
                    if (isValid(board, i, j, ch)) {
                        board[i][j] = ch;
                        if (solve(board)) return true;
                        board[i][j] = '.'; 
                    }
                }
                return false;
            }
        }
        return true;
    }

    private boolean isValid(char[][] board, int i, int j, char ch) {
        int row = 3 * (i / 3), col = 3 * (j / 3);
        for (int k = 0; k < 9; k++) {
            if (board[i][k] == ch || board[k][j] == ch) return false;
            if (board[row + k / 3][col + k % 3] == ch) return false;
        }
        return true;
    }
}