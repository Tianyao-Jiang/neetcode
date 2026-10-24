class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        left_count = 0
        right_count = 0 

        res = []
        path = []

        self.backtrack(n, path, res, 0, 0)

        return res

    def backtrack(self, n, path, res, left_count, right_count):

        if len(path) == 2 * n:
            res.append(''.join(path))
            return

     
        if left_count < n:
            path.append('(')
            self.backtrack(n, path, res, left_count + 1, right_count)
            path.pop()
            
        if right_count < left_count:
            path.append(')')
            self.backtrack(n, path, res, left_count, right_count + 1)
            path.pop()
        
