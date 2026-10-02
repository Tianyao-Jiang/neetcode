class Solution:
    DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    res += 1
                    self.dfs(r, c, visited, grid)
        return res

    def dfs(self, r, c, visited, grid):
        visited[r][c] = True

        for d in self.DIRS:
            nr = r + d[0]
            nc = c + d[1]

            if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]) and not visited[nr][nc] and grid[nr][nc] == '1':
                self.dfs(nr, nc, visited, grid) 


