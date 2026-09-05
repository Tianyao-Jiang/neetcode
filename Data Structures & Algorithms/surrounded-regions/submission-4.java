class Solution {
    int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int cols;
    int rows;
    boolean escaped;
    public void solve(char[][] board) {
        rows = board.length;
        cols = board[0].length;
        boolean[][] visited = new boolean[rows][cols];
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                List<int[]> res = new ArrayList<>();
                
                if (board[r][c] == 'O') {
                    if (board[r][c] != 'O' || visited[r][c]) continue;
                    escaped = false;
                    
                    bfs(board, r, c, visited, res);
                    if (!escaped) {
                        for(int i = 0; i < res.size(); i++) {
                            board[res.get(i)[0]][res.get(i)[1]] = 'X';
                        }

                    }
                }
            }
        }
    }

    private void bfs(char[][] board, int r, int c, boolean[][] visited, List<int[]> res) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{r, c});
        visited[r][c] = true;
        res.add(new int[]{r, c});

        while(!q.isEmpty()) {
            int[] node = q.poll();

            for (int[] dir: dirs) {
                int nr = node[0] + dir[0];
                int nc = node[1] + dir[1];
                if (nr < 0 || nc < 0|| nr >= rows || nc >= cols) {
                    escaped = true;
                    continue;
                }
                if (visited[nr][nc] || board[nr][nc] == 'X') {
                    continue;
                }

                q.add(new int[]{nr, nc});
                visited[nr][nc] = true;
                res.add(new int[]{nr, nc});
            }
        }
    } 
}
