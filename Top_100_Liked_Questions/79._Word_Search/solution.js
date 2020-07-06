/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    // backtracking
    let numRow = board.length;
    let numCol = board[0].length;
    
    let backtrack = function(r, c, i) {
        if (i === word.length) {
            return true;
        }
        
        if (r < 0 || r > numRow-1 || c < 0 || c > numCol-1 || board[r][c] != word[i]) {
            return false;
        }
        
        let ret = false;
        board[r][c] = '#';
        for (let [ro, co] of [[0,1], [1,0], [0,-1], [-1,0]]) {
            ret = backtrack(r+ro, c+co, i+1);
            if (ret) {
                break;
            }
        }
        
        board[r][c] = word[i];
        return ret;
    }
    
    for (let r=0; r<numRow; r++) {
        for (let c=0; c<numCol; c++) {
            if (backtrack(r, c, 0)) {
                return true;
            }
        }
    }
    
    return false;
};