class Solution {
    private int[][] dirs = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

    public int numIslands(char[][] grid) {
        // use BFS
        int res = 0;
        int row = grid.length;
        int col = grid[0].length;
        
        for(int i = 0; i < row; i++) {
            for(int j = 0; j < col; j++) {
                if (grid[i][j] == '1') {
                    bfs(grid, i, j);
                    res++;
                }
            }
        }

        return res;   
    }

    private void bfs(char[][] grid, int r, int c) {
        grid[r][c] = '0';
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{r, c});
        while(!queue.isEmpty()) {
            int[] node = queue.poll();
            int row = node[0];
            int col = node[1];

            for (int[] dir: dirs) {
                int nr = row + dir[0];
                int nc = col + dir[1];

                if (nr < grid.length && nc < grid[0].length && nr >= 0 && nc >= 0 && grid[nr][nc] == '1') {
                    queue.add(new int[]{nr, nc});
                    grid[nr][nc] = '0';
                }
            }
        }
    }
}
