class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        fresh = 0

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        res = 0
        while q and fresh > 0 :
            for i in range(len(q)):
                r, c = q.popleft()

                for dir in dirs:
                    nr = dir[0] + r
                    nc = dir[1] + c 

                    if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        visited.add((nr, nc))
                        fresh -= 1
            res += 1
        return res if fresh == 0 else -1 
