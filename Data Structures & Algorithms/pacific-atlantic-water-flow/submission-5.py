class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pac_visited = [[False for _ in range(cols)] for _ in range(rows)]
        alt_visited = [[False for _ in range(cols)] for _ in range(rows)]
        res = []

        for r in range(rows):
            self.dfs(r, 0, pac_visited, 0, heights)
            self.dfs(r, cols - 1, alt_visited, 0, heights)

        for c in range(cols):
            self.dfs(0, c, pac_visited, 0, heights)
            self.dfs(rows - 1, c, alt_visited, 0, heights)

        for i in range(rows):
            for j in range(cols):
                if pac_visited[i][j] and alt_visited[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, r, c, visited, prev_height, grid):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or visited[r][c] or grid[r][c] < prev_height:
            return

        visited[r][c] = True

        self.dfs(r + 1, c, visited, grid[r][c], grid)
        self.dfs(r - 1, c, visited, grid[r][c], grid)
        self.dfs(r, c + 1, visited, grid[r][c], grid)
        self.dfs(r, c - 1, visited, grid[r][c], grid)