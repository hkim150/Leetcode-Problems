/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let num_rows = grid.length;
    if (num_rows < 1) {
        return 0;
    }
    
    let num_cols = grid[0].length;
    if (num_cols < 1) {
        return 0;
    }
    
    let dfs_fill = function(row, col) {
        let stack = [[row, col]];
        
        while (stack.length) {
            let [r,c] = stack.pop();
            grid[r][c] = '2';
            
            if (c+1 < num_cols && grid[r][c+1] === '1') {
                stack.push([r, c+1]);
            }
            if (r+1 < num_rows && grid[r+1][c] === '1') {
                stack.push([r+1, c]);
            }
            if (c > 0 && grid[r][c-1] === '1') {
                stack.push([r, c-1]);
            }
            if (r > 0 && grid[r-1][c] === '1') {
                stack.push([r-1, c]);
            }
        }
    }
    
    let bfs_fill = function(row, col) {
        let stack = [[row, col]];
        grid[row][col] = '2';
        
        while (stack.length) {
            let [r,c] = stack.pop();
            
            if (c+1 < num_cols && grid[r][c+1] === '1') {
                stack.push([r, c+1]);
                grid[r][c+1] = '2';
            }
            if (r+1 < num_rows && grid[r+1][c] === '1') {
                stack.push([r+1, c]);
                grid[r+1][c] = '2';
            }
            if (c > 0 && grid[r][c-1] === '1') {
                stack.push([r, c-1]);
                grid[r][c-1] = '2';
            }
            if (r > 0 && grid[r-1][c] === '1') {
                stack.push([r-1, c]);
                grid[r-1][c] = '2';
            }
        }
    }
    
    let num_islands = 0;
    for (let r=0; r<num_rows; r++) {
        for (let c=0; c<num_cols; c++) {
            if (grid[r][c] === '1') {
                //dfs_fill(r, c);
                bfs_fill(r, c);
                num_islands++;
            }
        }
    }
    
    return num_islands;
};