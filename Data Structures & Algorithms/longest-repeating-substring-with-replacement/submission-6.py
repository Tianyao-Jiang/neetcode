class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = {}
        l = 0
        r = 0

        res = 0

        while r < len(s):
            m[s[r]] = m.get(s[r], 0) + 1

            while r - l + 1- max(m.values()) > k:
                m[s[l]] = m[s[l]] - 1
                l += 1
                
            res = max(res, r - l + 1)
            r += 1

        return res

