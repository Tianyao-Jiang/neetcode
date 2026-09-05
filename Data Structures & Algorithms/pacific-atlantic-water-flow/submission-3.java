class Solution {
    int rows;
    int cols;
    int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        rows = heights.length;
        cols = heights[0].length;
        boolean[][] pac = new boolean[rows][cols];
        boolean[][] atl = new boolean[rows][cols];

        for (int i = 0; i < rows; i++) {
            dfs(heights, pac, i, 0);
            dfs(heights, atl, i, cols - 1);
        }

        for (int j = 0; j < cols; j++) {
            dfs(heights, pac, 0, j);
            dfs(heights, atl, rows - 1, j);
        }

        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (pac[i][j] && atl[i][j]) {
                    res.add(Arrays.asList(i, j));
                }
            }
        }

        return res;
    }

    private void dfs(int[][] heights, boolean[][] ocean, int r, int c) {
        ocean[r][c] = true;

        for (int[] dir: dirs) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            if (nr >= 0 && nc >= 0 && nr < rows && nc < cols && heights[nr][nc] >= heights[r][c] && !ocean[nr][nc]) {
                dfs(heights, ocean, nr, nc);
            }
        }
    }
}
