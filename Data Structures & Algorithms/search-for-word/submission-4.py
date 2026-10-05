class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if self.dfs(board, r, c, 0, word, visited):
                    return True
        return False

    def dfs(self, board, r, c, idx, word, visited):
        if idx == len(word):
            return True
            
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or visited[r][c] or board[r][c] != word[idx]:
            return False
        

        visited[r][c] = True
        found = self.dfs(board, r+1, c, idx + 1, word, visited) or self.dfs(board, r - 1, c, idx + 1, word, visited) or self.dfs(board, r, c + 1, idx + 1, word, visited) or self.dfs(board, r, c - 1, idx + 1, word, visited) 
        visited[r][c] = False

        return found
        