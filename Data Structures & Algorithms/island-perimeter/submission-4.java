class Solution {
    private int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int islandPerimeter(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        int res = 0;
        for(int i = 0; i < grid.length; i++) {
            for(int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    q.add(new int[]{i, j});
                    visited[i][j] = true;
                    res += bfs(grid, q, visited);
                }
            }
        }

        return res;
    }

    private int bfs (int[][] grid, Queue<int[]> q, boolean[][] visited) {
        int res = 0;
        while (!q.isEmpty()) {
            int[] node = q.poll();
            for (int[] dir: dirs) {
                int nr = node[0] + dir[0];
                int nc = node[1] + dir[1];

                if (nr >= 0 && nc >= 0 && nr < grid.length && nc < grid[0].length && grid[nr][nc] == 1 && !visited[nr][nc]) {
                    q.add(new int[]{nr, nc});
                    visited[nr][nc] = true;
                } else if (nr < 0 || nc < 0 || nr>= grid.length || nc >= grid[0].length || grid[nr][nc] == 0) {
                    res++;
                }
            }
        }

        return res;
    }
}