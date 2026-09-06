class Solution {
    int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int rows;
    int cols;
    boolean found;
    boolean[][] visited; 
    public boolean exist(char[][] board, String word) {
        rows = board.length;
        cols = board[0].length;
        visited = new boolean[rows][cols];
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (dfs(board, r, c, 0, word)) {
                    return true;
                }
            }
        }

        return false;
    }

    private boolean dfs(char[][] board, int r, int c, int i, String word) {
        if (i == word.length()) {
            return true;
        }


        if (r < 0 || c < 0 || r >= rows || c >= cols) {
            return false;
        }

        if (board[r][c] != word.charAt(i) || visited[r][c]) {
            return false;
        }

        boolean res = false;
        for (int[] dir: dirs) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            
            visited[r][c] = true;
            res = res || dfs(board, nr, nc, i + 1, word);
            visited[r][c] = false;
        }
        return res;
    }
}
