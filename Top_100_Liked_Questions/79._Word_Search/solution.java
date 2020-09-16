class Solution {
    public boolean exist(char[][] board, String word) {
        for (int row=0; row<board.length; row++) {
            for (int col=0; col<board[0].length; col++) {
                if (backtrack(board, row, col, word, 0))
                    return true;
            }
        }

        return false;
    }

    public boolean backtrack(char[][] board, int row, int col, String word, int idx) {
        if (board[row][col] != word.charAt(idx))
            return false;

        if (idx == word.length()-1)
            return true;

        char orig = board[row][col];
        board[row][col] = '_';

        if (col+1 < board[0].length && backtrack(board, row, col+1, word, idx+1)) {
            board[row][col] = orig;
            return true;
        }

        if (row+1 < board.length && backtrack(board, row+1, col, word, idx+1)) {
            board[row][col] = orig;
            return true;
        }

        if (col-1 >= 0 && backtrack(board, row, col-1, word, idx+1)) {
            board[row][col] = orig;
            return true;
        }

        if (row-1 >= 0 && backtrack(board, row-1, col, word, idx+1)) {
            board[row][col] = orig;
            return true;
        }

        board[row][col] = orig;
        return false;
    }
}