class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        ## we use the most frequent char to replace

        count = {}
        l = 0
        r = 0
        res = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1

            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
            