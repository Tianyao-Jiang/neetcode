class Solution {
    int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    boolean pacific;
    boolean atlantic;
    int rows;
    int cols;

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        rows = heights.length;
        cols = heights[0].length;
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                pacific = false;
                atlantic = false;
                boolean[][] seen = new boolean[rows][cols];
                dfs(i, j, heights, seen, Integer.MAX_VALUE);
                if (pacific && atlantic) {
                    res.add(Arrays.asList(i, j));
                }
            }
        }

        return res;
    }

    private void dfs(int r, int c, int[][] heights, boolean[][] seen, int prevVal) {
        if (r < 0 || c < 0) {
            pacific = true;
            return;
        }

        if (r >= rows || c >= cols) {
            atlantic = true;
            return;
        }

        if (seen[r][c] || heights[r][c] > prevVal) return;
        seen[r][c] = true;  
        for (int[] d: dirs) {
             dfs(r + d[0], c + d[1], heights, seen, heights[r][c]);
            if (pacific && atlantic) return;
        }
    }
}
