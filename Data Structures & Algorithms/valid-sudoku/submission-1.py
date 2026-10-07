class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            s = set()
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in s:
                    return False
                else:
                    s.add(board[r][c])
            
        for c in range(cols):
            row_set = set()
            for r in range(rows):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row_set:
                    return False
                else:
                    row_set.add(board[r][c])

        set_list = [set() for _ in range(9)]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                r_ = r // 3
                c_ = c // 3

                if board[r][c] in set_list[r_ * 3 + c_]:
                    return False
                else:
                    set_list[r_ * 3 + c_].add(board[r][c])

        return True
