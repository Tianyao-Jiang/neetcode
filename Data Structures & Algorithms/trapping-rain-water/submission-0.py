class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n

        for i in range(n):
            if i == 0:
                prefix[i] = height[i]
                continue
            prefix[i] = max(prefix[i - 1], height[i])

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                suffix[i] = height[i]
                continue
            suffix[i] = max(suffix[i + 1], height[i])

        res = 0

        for i in range(n):
            cur = min(suffix[i], prefix[i]) - height[i]
            res += cur

        return res