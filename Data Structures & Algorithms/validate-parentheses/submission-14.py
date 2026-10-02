class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {')' : '(',
        ']' : '[',
        '}' : '{',
        }

        i = 0
        while i < len(s):
            cur = s[i]

            if cur == '(' or cur == '[' or cur == '{':
                stack.append(cur)
            else:
                if not stack or stack[-1] != m[cur]:
                    return False
                stack.pop()
            i += 1
        return len(stack) == 0 