class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = {
            '+',
            '-',
            '*',
            '/'
        }
        for token in tokens:
            if token in operators:
                right = int(stack.pop())
                left = int(stack.pop())
                res = 0

                if token == '+':
                    res = left + right
                elif token == '-':
                    res = left - right
                elif token == '*':
                    res = left * right
                else:
                    res = left / right
                stack.append(res)

            else:
                stack.append(token)

        return int(stack[0])