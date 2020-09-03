class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int row=0; row<grid.length; row++) {
            for (int col=0; col<grid[0].length; col++) {
                if (grid[row][col] == '1') {
                    dfs(grid, row, col);
                    count++;
                }
            }
        }
        return count;
    }

    public void dfs(char[][] grid, int row, int col) {
        Queue<Pos> q = new LinkedList<>();
        q.add(new Pos(row, col));
        grid[row][col] = '2';

        while (!q.isEmpty()) {
            Pos p = q.remove();

            if (p.col+1 < grid[0].length && grid[p.row][p.col+1] == '1') {
                q.add(new Pos(p.row, p.col+1));
                grid[p.row][p.col+1] = '2';
            }
            if (p.row+1 < grid.length && grid[p.row+1][p.col] == '1') {
                q.add(new Pos(p.row+1, p.col));
                grid[p.row+1][p.col] = '2';
            }
            if (p.col-1 >= 0 && grid[p.row][p.col-1] == '1') {
                q.add(new Pos(p.row, p.col-1));
                grid[p.row][p.col-1] = '2';
            }
            if (p.row-1 >= 0 && grid[p.row-1][p.col] == '1') {
                q.add(new Pos(p.row-1, p.col));
                grid[p.row-1][p.col] = '2';
            }
        }
    }
}

class Pos {
    public int row;
    public int col;

    public Pos(int row, int col) {
        this.row = row;
        this.col = col;
    }
}