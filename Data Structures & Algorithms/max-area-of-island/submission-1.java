class Solution {
    private int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public int maxAreaOfIsland(int[][] grid) {
        
        int res = 0;
        int row = grid.length;
        int col = grid[0].length;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    int curArea = bfs(grid, i, j);
                    res = Math.max(res, curArea);
                }
            }
        }
        return res;
    }

    private int bfs(int[][] grid, int r, int c) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{r, c});
        grid[r][c] = 0;
        int res = 1;

        while(!q.isEmpty()) {
            int[] node = q.poll();
            for (int[] dir: dirs) {
                int nr = node[0] + dir[0];
                int nc = node[1] + dir[1];

                if (nr >= 0 && nc >= 0 && nr < grid.length && nc < grid[0].length && grid[nr][nc] == 1) {
                    q.add(new int[]{nr, nc});
                    grid[nr][nc] = 0;
                    res++;
                }
            }
        }

        return res;
    }
}
