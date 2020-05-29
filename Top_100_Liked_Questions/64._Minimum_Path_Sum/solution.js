/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    // dp with mem
    let h = grid.length;
    let w = grid[0].length;
    
    let mem = new Array(h+1);
    
    for (let row=0; row<h+1; row++) {
        if (row < h) {
            mem[row] = new Array(w+1).fill(0);
            mem[row][w] = Infinity;
        } else {
            mem[row] = new Array(w+1).fill(Infinity);
        }
    }
    
    for (let row=h-1; row>-1; row--) {
        for (let col=w-1; col>-1; col--) {
            if (row == h-1 && col == w-1) {
                mem[row][col] = grid[row][col];
                continue;
            }
            
            mem[row][col] = grid[row][col] + Math.min(mem[row+1][col], mem[row][col+1]);
        }
    }
    
    return mem[0][0];
}

var minPathSum2 = function(grid) {
    // recursive naive solution
    let helper = function(row, col) {
        if (row == grid.length-1 && col == grid[0].length-1) {
            return grid[row][col];
        }
        
        let down = row < grid.length-1 ? helper(row+1, col) : Infinity;
        let right = col < grid[0].length-1 ? helper(row, col+1) : Infinity;
        
        return grid[row][col] + Math.min(down, right);
    }
    
    return helper(0,0);
};