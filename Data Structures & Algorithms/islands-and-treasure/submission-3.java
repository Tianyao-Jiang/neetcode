class Solution {
    private int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public void islandsAndTreasure(int[][] grid) {
        
        int row = grid.length;
        int col = grid[0].length;
        Queue<int[]> q = new LinkedList<>();

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 0) {
                    q.add(new int[]{i, j});
                }
            }
        }

        bfs(grid, q);
    }

    private void bfs(int[][] grid, Queue<int[]> q) {
        int count = 1;

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i< size; i++) {
                int[] node = q.poll();
                int r = node[0];
                int c = node[1];
                for (int[] dir : dirs) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];
                    if (nr >= 0 && nc >=0 && nr < grid.length && nc < grid[0].length && grid[nr][nc] == Integer.MAX_VALUE) {
                        q.add(new int[]{nr, nc});
                        grid[nr][nc] = count;
                    }
                }
            }
            count++;
        }
    }
}
