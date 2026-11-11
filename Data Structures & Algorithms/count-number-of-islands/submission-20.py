class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = 0 

        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0" or (r, c) in visited:
                return
            
            visited.add((r, c))
            
            for dir in dirs:
                dfs(r + dir[0], c + dir[1])

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    res += 1

        return res 


