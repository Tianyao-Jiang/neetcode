class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        
        cur_max = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            if count[s[r]] > 1:
                while count[s[r]] > 1:
                    count[s[l]] -= 1
                    l += 1
            cur_max = max(cur_max, r - l + 1)

        return cur_max