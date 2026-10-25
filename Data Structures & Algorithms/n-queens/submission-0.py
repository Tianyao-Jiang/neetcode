class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col_set = set()
        pos_dia_set = set() # r + c        
        neg_dia_set = set() # r - c
        
        grid = [['.' for c in range(n)] for r in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in grid]
                res.append(copy)
                return

            for c in range(n):
                if c in col_set or r + c in pos_dia_set or r - c in neg_dia_set:
                    continue
                grid[r][c] = 'Q'
                col_set.add(c)
                pos_dia_set.add(r + c)
                neg_dia_set.add(r - c)
                backtrack(r + 1)

                grid[r][c] = '.'
                col_set.remove(c)
                pos_dia_set.remove(r + c)
                neg_dia_set.remove(r - c)

        backtrack(0)

        return res                


