class Solution {
    private int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int orangesRotting(int[][] grid) {
        // bfs to solve this problem
        // if node is 2. push to queue
        // push the surronding queue if the node is 1, change them to 2, and count++
        int row = grid.length;
        int col = grid[0].length;
        int count = 0;

        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 2) {
                    q.add(new int[]{i, j});
                    grid[i][j] = 0;
                }
            }
        }

        int res = bfs(grid, q);

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    return -1;
                }
            }
        }

        return res;
    }

    private int bfs(int[][] grid, Queue<int[]> q) {
        int count = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            boolean spread = false;
            for (int i = 0; i < size; i++) {
                int[] node = q.poll();
                int r = node[0];
                int c = node[1];
                for (int[] dir: dirs) {
                    int nr = node[0] + dir[0];
                    int nc = node[1] + dir[1];
                    if (nr >= 0 && nc >= 0 && nr < grid.length && nc < grid[0].length && grid[nr][nc] != 0) {
                        q.add(new int[]{nr, nc});
                        grid[nr][nc] = 0;
                        spread = true;
                        System.out.println("row" + nr + "col" + nc + "change" + 0);
                    }
                }
            }
            if (spread) count++;
        }
        return count;
    }
}
