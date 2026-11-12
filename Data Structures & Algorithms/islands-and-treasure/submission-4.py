class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dir in dirs:
                    nr = r + dir[0]
                    nc = c + dir[1]

                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and (nr, nc) not in visited and grid[nr][nc] != -1:
                        q.append((nr, nc))
                        visited.add((nr, nc))


            dist += 1