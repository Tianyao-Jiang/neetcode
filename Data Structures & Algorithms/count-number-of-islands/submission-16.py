class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            visited[r][c] = True

            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]

                if nr >= 0 and nc >= 0 and nr < rows and nc < cols and not visited[nr][nc] and grid[nr][nc] == '1':
                    dfs(nr, nc) 

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    res += 1
                    dfs(r, c)
        return res


