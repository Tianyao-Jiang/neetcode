class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = ""
        res = []
        self.backtrack(0, 0, n, path, res)
        return res

    def backtrack(self, left_count, right_count, n, path, res):
        if len(path) == 2 * n:
            res.append(path)
            return 

        if left_count > right_count:
            path += ')'
            self.backtrack(left_count, right_count + 1, n, path, res)
            path = path[:-1]
        
        if left_count < n:
            path += '('
            self.backtrack(left_count + 1, right_count, n, path, res)
            path = path[:-1]

